from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Author Schemas
class AuthorBase(BaseModel):
    name: str
    email_id: EmailStr  # Email validation
    phone_number: str = Field(..., pattern=r'^\+?\d{10,15}$')  # Basic phone number validation

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    name: str
    email: str
    phone_number: str
    created_at: datetime

    class Config:
        from_attributes = True

# Book Schemas
class BookBase(BaseModel):
    title: str
    author_id: int
    publisher_id: int

class BookCreate(BookBase):
    pass    

class BookResponse(BookBase):
    id: int
    title: str
    author_id: int
    publisher_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Publisher Schemas
class PublisherBase(BaseModel):
    name: str
    email_id: EmailStr  # Email validation
    phone_number: str = Field(..., pattern=r'^\+?\d{10,15}$')  # Basic phone number validation

class PublisherCreate(PublisherBase):
    pass

class PublisherResponse(PublisherBase):
    id: int
    name: str
    email: str
    phone_number: str
    created_at: datetime

    class Config:
        from_attributes = True
