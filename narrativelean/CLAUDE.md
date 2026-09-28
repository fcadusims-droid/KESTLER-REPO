# Regras de operação — NarrativeLean

Para qualquer sessão do Claude que trabalhe nesta pasta. O README explica o
sistema; este arquivo diz o que pode e o que não pode.

## Privacidade

- Esta pasta é privada. Não mencione o NarrativeLean no README da raiz, no
  site (`.vitepress/`, `index.md`), nas obras, em commits de outras áreas nem
  em textos públicos.
- Nunca crie arquivo `.md` na raiz do repositório: o site publica tudo que
  estiver lá. Cópias de teste, obras plantadas e rascunhos ficam aqui dentro.

## Hierarquia da verdade

1. O texto do autor.
2. Canon **aprovado** pelo autor (`canon/`, sem `proposto_por: claude`; regras
   com `formalizacao` só se `aprovada_hash` bater).
3. Fatos extraídos, com citação ancorada.
4. Qualquer coisa que o Claude "sabe" sobre a obra. Isto não é evidência.

## O que o Claude nunca faz

- Rodar `regras aprovar` ou `canon aprovar`. Aprovar é do autor; o Claude
  propõe (`proposto_por: claude`, `formalizacao: {proposta_por: claude}`) e
  para.
- Alterar canon aprovado. Pode propor mudança, com o motivo, para o autor.
- Plantar erros ou escrever itens do golden set com `origem: autor`. O que o
  Claude escrever leva `origem: claude` e não conta como validação.
- Editar a obra para "resolver" um diagnóstico. Diagnóstico é indício, não
  ordem, e não existe meta de zerar o relatório.
- Criar conteúdo novo na obra (personagem, evento, regra, explicação). Conteúdo
  novo só nasce de direção explícita do autor.
- Subir nível de diagnóstico, ou emitir ERROR de lente semântica. Método próprio
  (sem fonte publicada) fica em SUGGESTION.
- Escrever lente semântica sem contrato. Contrato primeiro
  (`verifiers/semantic/contracts/`), com teste de violação intencional; só
  depois o código. `nl.py contratos` valida.
- Mexer em `facts/` ou `cache/` à mão. Só a ingestão escreve lá.

## Operando pacotes à mão

Quando não houver `claude -p` e o Claude interativo for o operador:

- Um pacote de cada vez: ler `work/pendentes/<X>.md`, responder em
  `work/respostas/<X>.yaml` exatamente no formato que o pacote pede.
- Responder só com o que está no pacote. Não abrir a obra, o canon, os fatos
  nem o relatório para "ajudar": isso contamina a extração, e o
  que se mede é o extrator sozinho.
- Citação literal, copiada do texto do pacote. Nunca número de linha (o código
  calcula). Na dúvida entre dois modos, o menos forte (`fala`, `pensamento`,
  `documento_interno`) e `confianca_extracao: baixa`.
- Extração aberta e dirigida da mesma unidade na mesma sessão tornam a
  divergência entre elas sem sentido. Numa rodada que conta como medição, use
  `extrair rodar` (um processo por pacote) ou sessões novas.

## Advogado do diabo

- Sessão separada da que gerou o relatório (`extrair rodar --fila advogado`).
- Vereditos: MANTER, REENQUADRAR, REBAIXAR, CONTESTAR. Nunca apaga um
  diagnóstico, nunca sobe para ERROR, nunca escreve na obra.
- Todo argumento precisa de citação ancorada; sem ela, a ingestão descarta.

## Edições

- Qualquer edição de obra sugerida a partir do relatório vai para um branch,
  nunca direto no `main`, e só depois de o autor escolher qual trecho está
  certo.
- Mudou um prompt: novo arquivo (`prompts/<nome>_v2.md`) e troca em
  `project.yaml`. Nunca editar um prompt em uso no lugar.

## Parâmetros por tipo de documento

| Tipo | Unidade | O que roda hoje |
|---|---|---|
| prosa | seção e quebra de cena | formais (timeline, regras, atributos, regra × regra) |
| roteiro | seção e cena `INT.`/`EXT.` | formais |
| biblia | seção (título até `###`) | formais + referência sem definição |
| ficha, cronologia | seção | formais |
| ramificado | seção e quebra de cena | nada: os fatos ficam de fora até existir verificação por estado |

As lentes semânticas estão em `lenses.yaml` (tabela da seção 4.3), mas só rodam
depois de implementadas com contrato. Documento com classificação `baixa` não
roda: o autor declara o tipo em `doctypes.yaml`.

## Antes de commitar

```bash
python narrativelean/nl.py validar
python -m unittest discover -s narrativelean/tests/verifiers
```
