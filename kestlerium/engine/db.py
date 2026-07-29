"""Acesso ao SQLite. Uma conexão, um schema, nenhum ORM."""

from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema.sql"
DEFAULT_DB = ROOT / "out" / "kestlerium.db"


def connect(db_path: Path | str = DEFAULT_DB, fresh: bool = False) -> sqlite3.Connection:
    """Abre (e cria) o banco. `fresh=True` apaga e recomeça do zero."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if fresh:
        for suffix in ("", "-wal", "-shm"):
            candidate = Path(str(path) + suffix)
            if candidate.exists():
                candidate.unlink()

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    # A simulação é reprodutível pela seed; o banco é descartável. Trocar
    # durabilidade por velocidade aqui é seguro.
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = OFF")
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    _migrar(conn)
    return conn


# Colunas acrescentadas depois que o mundo já estava rodando. `CREATE TABLE IF
# NOT EXISTS` não altera tabela existente — o banco da vila é versionado e
# sobrevive de uma execução para a outra, então uma coluna nova quebraria o
# agendador em produção enquanto a validação (que roda em banco novo) passaria
# tranquila. Aconteceu exatamente assim com `facts_json`.
COLUNAS_NOVAS = [
    ("pressure_event", "facts_json", "TEXT"),
    ("scheduled", "facts_json", "TEXT NOT NULL DEFAULT '[]'"),
]


def _migrar(conn: sqlite3.Connection) -> None:
    for tabela, coluna, tipo in COLUNAS_NOVAS:
        existentes = {r[1] for r in conn.execute(f"PRAGMA table_info({tabela})")}
        if coluna not in existentes:
            conn.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo}")
    conn.commit()
