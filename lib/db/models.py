from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")
    sales = relationship("Sale", back_populates="book")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship("Book", back_populates="sales")
