from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Text, 
    ForeignKey
)

from datetime import datetime

from database.database import Base



class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class Chat(Base):

    __tablename__ = "chats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    query = Column(
        Text
    )

    response = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Report(Base):

    __tablename__="reports"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    engine_id = Column(
        Integer
    )


    report_text = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    filename = Column(
        String
    )

    filepath = Column(
        String
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )