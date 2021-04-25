from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    """Users of the system."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Location(Base):
    """Keeps the full path of stored files, and the folder name they are in."""
    __tablename__ = "location"

    folder_name = Column(String, primary_key=True, index=True)
    full_path = Column(String)

    receipt_relation = relationship("Receipt")
    # receipt_relation = relationship("Receipt", backpopulates="location_relation")


class Receipt(Base):
    """Receipts for things you have bought."""
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    filename = Column(String)
    location = Column(String, ForeignKey("location.folder_name"))

    # location_relation = relationship("Location", backpopulates="receipt_relation")
    book_relation = relationship("Book")
    movie_relation = relationship("Movie")


class Book(Base):
    """Your books."""
    __tablename__ = "book"

    isbn = Column(String, primary_key=True, index=True)
    title = Column(String)
    edition = Column(Integer)
    author = Column(String)
    publisher = Column(String)
    pages = Column(Integer)
    cover = Column(String)
    genre = Column(String)
    receipt = Column(Integer, ForeignKey("receipt.id"))

    # wishlist_row = relationship("Wishlist", backpopulates="book")
    # receipt_rel = relationship("Receipt", backpopulates="")


class Movie(Base):
    """Your movies."""
    __tablename__ = "movie"

    title = Column(String, primary_key=True, index=True)
    age = Column(String)
    genre = Column(String)
    format = Column(String)  # DVD, VHS, BlueRay etc.
    receipt = Column(Integer, ForeignKey("receipt.id"))

    # wishlist_row_movie = relationship("Wishlist", backpopulates="movie")


'''
class Wishlist(Base):
    """Stuff you wish for"""
    __tablename__ = "wishlist"

    user = Column(Integer, primary_key=True, index=True)
    event = Column(String, primary_key=True)
    book_isbn = Column(Integer, ForeignKey("book.isbn"))  # Foreign key
    movie_title = Column(String, ForeignKey("movie.title"))  # Foreign key

    book = relationship("Book", backpopulates="wishlist_row_book")
    movie = relationship("Movie", backpopulates="wishlist_row_movie")


class Contents(Base):
    """List of stuff you have in your house."""
    __tablename__ = "contents"  # Stuff you have in your house

    item = Column(String, primary_key=True, index=True)
    type = Column(String)  # Couch, TV, table, etc.
    description = Column(String)
    approximate_value = Column(Float)
    location = Column(String)
    acquired = Column(Date)


class Recipe(Base):
    """Stores recipes."""
    __tablename__ = "recipe"

    name = Column(String, primary_key=True, index=True)
    ingredients = Column(String)
    procedure = Column(Text)


class Bill(Base):
    """Stores your bills."""
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    biller = Column(String)
    amount = Column(Float)
    kid = Column(String)
    due = Column(Date)
    payed = Column(Boolean, default=False)  # If registered when the bill arrive, and before it has been payed.
    date_payed = Column(Date, default=None)  # Use trigger to fill in?

'''