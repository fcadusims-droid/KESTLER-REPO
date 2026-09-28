"""Operador: quem lê linguagem. Um processo novo por pacote.

O sistema não chama API nenhuma. Ele entrega cada pacote a um comando externo
e lê a resposta. O comando pode ser:

- `claude -p` — o Claude Code em modo não interativo (usa o plano do autor,
  sem chave de API);
- um modelo aberto e gratuito rodando local, por exemplo
  `ollama run qwen2.5:14b` ou `llama-cli -m modelo.gguf -f {arquivo}`;
- nada: um Claude Code interativo lê `work/pendentes/` e escreve
  `work/respostas/` à mão (ver CLAUDE.md).

Um processo por pacote é o que faz das "sessões separadas" (seção 9) uma
propriedade da arquitetura, e não uma promessa: o operador que extrai uma
unidade nunca viu o relatório anterior, a edição, nem outra unidade.

E o processo roda numa pasta temporária VAZIA, não no repositório: um
`claude -p` aberto aqui dentro poderia ler o canon, os relatórios e as outras
unidades por conta própria (e carregaria o CLAUDE.md desta pasta). Fora do
repositório, tudo o que ele sabe é o que está no pacote.
"""

from __future__ import annotations

import shlex
import subprocess
import tempfile
from pathlib import Path

from .extraction import PENDENTES, RESPOSTAS


def pendentes_sem_resposta(pasta: Path = PENDENTES, respostas: Path = RESPOSTAS) -> list[Path]:
    if not pasta.exists():
        return []
    saida = []
    for pacote in sorted(pasta.glob("*.md")):
        if not any((respostas / f"{pacote.stem}{ext}").exists() for ext in (".yaml", ".md", ".txt")):
            saida.append(pacote)
    return saida


def rodar(comando: str, limite: int | None = None, tempo_limite: int = 900,
          pasta: Path = PENDENTES, respostas: Path = RESPOSTAS) -> dict:
    """Roda o comando uma vez por pacote pendente.

    O pacote vai pela entrada padrão; se o comando tiver `{arquivo}`, o caminho
    do pacote é passado no lugar. A saída padrão inteira vira a resposta — a
    ingestão depois extrai o bloco YAML dela.
    """
    respostas.mkdir(parents=True, exist_ok=True)
    feitos, falhas = 0, []
    for pacote in pendentes_sem_resposta(pasta, respostas)[: limite or None]:
        pacote = pacote.resolve()
        texto = pacote.read_text(encoding="utf-8")
        if "{arquivo}" in comando:
            args = shlex.split(comando.replace("{arquivo}", shlex.quote(str(pacote))))
            entrada = None
        else:
            args = shlex.split(comando)
            entrada = texto
        try:
            with tempfile.TemporaryDirectory(prefix="nlean-operador-") as vazia:
                r = subprocess.run(args, input=entrada, capture_output=True, text=True,
                                   timeout=tempo_limite, cwd=vazia)
        except (OSError, subprocess.TimeoutExpired) as erro:
            falhas.append(f"{pacote.stem}: {erro}")
            continue
        if r.returncode != 0 or not r.stdout.strip():
            falhas.append(f"{pacote.stem}: código {r.returncode}; {r.stderr.strip()[:200]}")
            continue
        (respostas / f"{pacote.stem}.md").write_text(r.stdout, encoding="utf-8")
        feitos += 1
    return {"respondidos": feitos, "falhas": falhas,
            "restantes": len(pendentes_sem_resposta(pasta, respostas))}
