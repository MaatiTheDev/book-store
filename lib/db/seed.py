from lib.db.models import Author, Book, session

def seed_data():
    # Add some authors
    author1 = Author(name="George Orwell")
    author2 = Author(name="J.K. Rowling")

    # Add some books
    book1 = Book(title="1984", author=author1)
    book2 = Book(title="Animal Farm", author=author1)
    book3 = Book(title="Harry Potter and the Sorcerer's Stone", author=author2)

    # Add data to session and commit
    session.add_all([author1, author2, book1, book2, book3])
    session.commit()
