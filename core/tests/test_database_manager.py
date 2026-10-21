"""
Test Suite for Database Class
=============================

This module contains unit tests for the `Database` class defined in `database_manager.py`.

Test Coverage
-------------
- Creating and reading language entries.
- Ignoring duplicates on create.
- Updating and deleting entries.
- Listing all stored languages.
- Creating or updating entries in a unified method.
- Using the class with a context manager.
"""

import pytest
from core.database_manager import Database


@pytest.fixture
def temp_db():
    """
    Provides a fresh in-memory SQLite database for each test to ensure isolation.
    Automatically closes the database after the test completes.
    """
    db = Database(":memory:")
    yield db
    db.close()


def test_create_and_read_language(temp_db):
    """
    Test that a language can be created and then read from the database.
    """
    temp_db.create("Python", "<h1>Python</h1>")
    content = temp_db.read("Python")
    assert content == "<h1>Python</h1>"


def test_create_ignores_duplicate(temp_db):
    """
    Test that attempting to create a duplicate language does not overwrite existing data.
    """
    temp_db.create("Python", "first")
    temp_db.create("Python", "second")  # Should be ignored
    content = temp_db.read("Python")
    assert content == "first"


def test_update_language(temp_db):
    """
    Test that updating an existing language correctly changes its content.
    """
    temp_db.create("Python", "Old Content")
    temp_db.update("Python", "Updated Content")
    assert temp_db.read("Python") == "Updated Content"


def test_delete_language(temp_db):
    """
    Test that a language can be deleted and is no longer readable afterward.
    """
    temp_db.create("Python", "Some Content")
    temp_db.delete("Python")
    assert temp_db.read("Python") is None


def test_list_all(temp_db):
    """
    Test that all languages in the database can be listed.
    """
    temp_db.create("Python", "Py content")
    temp_db.create("JavaScript", "JS content")
    results = temp_db.list_all()
    names = [row[1] for row in results]
    assert "Python" in names
    assert "JavaScript" in names


def test_create_or_update(temp_db):
    """
    Test that the create_or_update method inserts if new, or updates if exists.
    """
    temp_db.create_or_update("C", "Initial")
    assert temp_db.read("C") == "Initial"

    temp_db.create_or_update("C", "Modified")
    assert temp_db.read("C") == "Modified"


def test_context_manager():
    """
    Test that the Database class works properly as a context manager.
    """
    with Database(":memory:") as db:
        db.create("Rust", "Safe and fast")
        assert db.read("Rust") == "Safe and fast"
