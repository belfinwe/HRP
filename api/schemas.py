import datetime
from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



# users
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True



class SwearJarDebt(BaseModel):
    amount: int


class SwearJarDebtRead(SwearJarDebt):
    person: int


"""
# bill table
class BillBase(BaseModel):
    biller: str
    amount: float
    kid: str
    due: date


class BillAdd(BillBase):
    pass


class BillUpdate(BillBase):
    payed: bool
    date_payed: date


class BillRead(BillBase):
    id: int
    payed: bool
    date_payed: date


# receipt table
class ReceiptBase(BaseModel):
    item: str
    filename: str


class ReceiptAdd(ReceiptBase):
    pass


class ReceiptRead(ReceiptBase):
    id: int
    location: str


class ReceiptUpdate(ReceiptBase):
    location: str


# book table
class BookBase(BaseModel):
    isbn: str
    title: str
    edition: int
    author: str
    publisher: str
    pages: int
    cover: str
    genre: str


class BookAdd(BookBase):
    pass


class BookRead(BookBase):
    pass


class BookUpdate(BookBase):
    receipt: int


# movie table
class MovieBase(BaseModel):
    title: str
    age: str
    genre: str
    format: str


class MovieAdd(MovieBase):
    pass


class MovieRead(MovieBase):
    pass


class MovieUpdate(MovieBase):
    receipt: int


"""