# Gabarito por pooling

Recall "de verdade" numa obra real não dá para medir sem saber quantos
problemas ela tem. O pooling (seção 11) aproxima isso juntando três fontes
independentes e pedindo ao autor que rotule cada candidato:

1. **manual** — `nl.py gabarito amostrar <obra.md> --n 5 --semente 1` sorteia
   unidades. O autor lê só essas, SEM olhar o relatório, e anota em
   `achados_manuais` o que achar (`linha_inicio`, `linha_fim`, `descricao`).
2. **pipeline** — os diagnósticos de `nl.py verificar`.
3. **baseline** — um modelo lendo a obra inteira de uma vez
   (`nl.py baseline preparar|ingerir <obra.md>`), só com citações ancoradas.

`nl.py gabarito juntar <obra.md>` funde as três em `pool.yaml`
(candidatos que se sobrepõem em linhas viram um só). O autor marca cada um com
`real: true` ou `real: false` (e `nota_autor`, se quiser). Rótulos já dados
sobrevivem a um novo `juntar`.

`nl.py gabarito pontuar <obra.md>` dá recall e precisão por fonte, com IC 95%
de Wilson, e quantos problemas reais só o pipeline achou, só o baseline achou,
ou os dois. Se o baseline acha quase tudo que o pipeline acha, o pipeline não
se paga.

Cada obra ganha uma subpasta aqui (`tests/gabarito/<obra>/`).
