"""Leitura e escrita dos arquivos do projeto. Nenhuma lógica de verificação aqui.

Tudo o que o autor edita é YAML; tudo o que o sistema grava também. Um formato
só, legível à mão, para que o autor consiga conferir qualquer coisa sem código.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import yaml

# narrativelean/ — a raiz do projeto de verificação.
RAIZ = Path(__file__).resolve().parent.parent


class ErroDeProjeto(Exception):
    """Configuração ou canon inválido. A mensagem diz o arquivo e o que corrigir."""


def carregar_yaml(caminho: Path | str, padrao=None):
    caminho = Path(caminho)
    if not caminho.exists():
        return padrao
    try:
        dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except yaml.YAMLError as erro:
        raise ErroDeProjeto(f"{caminho}: YAML inválido — {erro}") from erro
    return padrao if dados is None else dados


def salvar_yaml(caminho: Path | str, dados) -> None:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(
        yaml.safe_dump(dados, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


def salvar_json(caminho: Path | str, dados) -> None:
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def sha(texto: str, n: int = 16) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:n]


def sha_estavel(obj) -> str:
    """Hash de uma estrutura, independente da ordem das chaves."""
    return sha(json.dumps(obj, ensure_ascii=False, sort_keys=True, default=str))


def normalizar_nome(texto) -> str:
    """Forma de comparação de nomes: sem acento, sem caixa, espaços únicos.

    "Heitor", "heitor" e "HEITOR " são o mesmo personagem; "Heitor" e "Heitor
    Duarte" não, a menos que o canon declare o apelido.
    """
    if texto is None:
        return ""
    s = unicodedata.normalize("NFKD", str(texto))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\s_]+", " ", s.casefold()).strip()
    return s


def slug(texto: str) -> str:
    s = normalizar_nome(texto)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "sem-titulo"


@lru_cache(maxsize=1)
def projeto() -> dict:
    dados = carregar_yaml(RAIZ / "project.yaml")
    if not dados:
        raise ErroDeProjeto("narrativelean/project.yaml não encontrado")
    return dados


def raiz_obras() -> Path:
    return (RAIZ / projeto().get("obras_raiz", "..")).resolve()


def caminho_obra(arquivo: str) -> Path:
    """Arquivo de uma obra, relativo à raiz das obras.

    Caminhos que começam com `narrativelean/` (cópias com erros plantados, por
    exemplo) são resolvidos a partir da raiz do repositório normalmente — a raiz
    das obras É a raiz do repositório.
    """
    return raiz_obras() / arquivo


def ler_obra(arquivo: str) -> str:
    caminho = caminho_obra(arquivo)
    if not caminho.exists():
        raise ErroDeProjeto(f"obra não encontrada: {arquivo} (procurado em {caminho})")
    return caminho.read_text(encoding="utf-8")


def versao_atual() -> str:
    return str(projeto().get("versao_atual", "v1"))
