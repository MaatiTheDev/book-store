import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import click
from lib.db.models import Author, Book, Sale, session






from lib.db.models import Author, Book, Sale, session
from lib.db.seed import seed_data
from lib.helpers import add_book_helper, add_author_helper, list_books_helper

@click.group()
def cli():
    """Book Store Management CLI"""
    pass

@cli.command()
def seed():
    """Seed the database with initial data"""
    seed_data()
    click.echo("Database seeded with initial data.")

@cli.command()
@click.argument('name')
def add_author(name):
    """Add a new author"""
    add_author_helper(name)
    click.echo(f"Author {name} added to the database.")

@cli.command()
@click.argument('title')
@click.argument('author_name')
def add_book(title, author_name):
    """Add a new book"""
    add_book_helper(title, author_name)
    click.echo(f"Book {title} by {author_name} added to the database.")

@cli.command()
def list_books():
    """List all available books"""
    books = list_books_helper()
    click.echo("Books Available:")
    for book in books:
        click.echo(f"- {book.title} by {book.author.name}")

if __name__ == "__main__":
    cli()
