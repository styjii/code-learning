"""
database_manager.py
===================

This module provides a SQLite-backed database interface for storing and retrieving
Markdown-based language documentation converted to tabbed HTML.

It includes:
------------
- A `Database` class to manage the 'Language' table.
- Methods to create, read, update, delete, and list language entries.
- A `main()` function to populate the database from Markdown files.

Dependencies:
-------------
- Uses `PAGE_CONFIG` from `language.config` to get topic mappings.
- Uses `MarkdownToTabbedHTML` from `core.markdown_to_tabbed_html` to convert Markdown to HTML.

Typical usage:
--------------
    from database_manager import Database

    with Database() as db:
        html = db.read("Python")
"""

import sqlite3
from sqlite3 import Connection
from typing import Optional, List, Tuple
from pathlib import Path
from language.config import PAGE_CONFIG


class Database:
    """SQLite database wrapper for Language table operations."""

    def __init__(self, db_path: Path = Path(__file__).resolve().parent.parent / "languages.sqlite3") -> None:
        self.db_path = db_path
        self.conn: Connection = sqlite3.connect(self.db_path)
        self._ensure_table_exists()

    def _ensure_table_exists(self) -> None:
        """Create the Language table if it doesn't exist."""
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS Language (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    content TEXT,
                    signature TEXT
                );
                """
            )
            # Bases créées avant l'ajout de la colonne « signature ».
            columns = {row[1] for row in self.conn.execute("PRAGMA table_info(Language)")}
            if "signature" not in columns:
                self.conn.execute("ALTER TABLE Language ADD COLUMN signature TEXT")

    def create(self, name: str, content: Optional[str] = None) -> None:
        """Insert a new language entry (ignoring if name exists)."""
        with self.conn:
            self.conn.execute(
                "INSERT OR IGNORE INTO Language (name, content) VALUES (?, ?)",
                (name, content),
            )

    def read(self, name: str) -> Optional[str]:
        """Retrieve the content of a language by name."""
        cursor = self.conn.execute(
            "SELECT content FROM Language WHERE name = ?",
            (name,),
        )
        row = cursor.fetchone()
        return row[0] if row else None

    def update(self, name: str, new_content: str) -> None:
        """Update the content of an existing language."""
        with self.conn:
            self.conn.execute(
                "UPDATE Language SET content = ? WHERE name = ?",
                (new_content, name),
            )

    def delete(self, name: str) -> None:
        """Delete a language entry by name."""
        with self.conn:
            self.conn.execute(
                "DELETE FROM Language WHERE name = ?",
                (name,),
            )

    def list_all(self) -> List[Tuple[int, str, Optional[str]]]:
        """Return a list of all languages as (id, name, content)."""
        cursor = self.conn.execute(
            "SELECT id, name, content FROM Language"
        )
        return cursor.fetchall()

    def create_or_update(self, name: str, content: str, signature: Optional[str] = None) -> None:
        """Create a new language or update it if it already exists."""
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO Language (name, content, signature) VALUES (?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET content = excluded.content, signature = excluded.signature
                """,
                (name, content, signature),
            )

    def get_signature(self, name: str) -> Optional[str]:
        """Return the signature stored with an entry (None if missing or unsigned)."""
        row = self.conn.execute("SELECT signature FROM Language WHERE name = ?", (name,)).fetchone()
        return row[0] if row else None

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


def main() -> None:
    """Generate tabbed HTML from markdown topics and store/update them in the database."""
    from language.services import get_page_html

    for key in PAGE_CONFIG:
        get_page_html(key, force=True)
        print(f"Traité et enregistré : {key}")


if __name__ == '__main__':
    main()
