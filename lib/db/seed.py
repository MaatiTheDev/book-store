from models import Author, Book, session

# Create some authors
author1 = Author(name="John Steinbeck")
author2 = Author(name="George Orwell")

# Create some books
book1 = Book(title="Of Mice and Men", author=author1)
book2 = Book(title="1984", author=author2)

# Add authors and books to the session
session.add_all([author1, author2, book1, book2])

# Commit the changes to the database
session.commit()

print("Database seeded successfully!")
