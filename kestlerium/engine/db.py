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
    return conn
