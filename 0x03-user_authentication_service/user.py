#!/usr/bin/env python3
"""
User model definition for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for declarative models
Base = declarative_base()

class User(Base):
    """
    SQLAlchemy User model that represents the 'users' table.
    Attributes:
        id (int): The user's primary key.
        email (str): The user's email (non-nullable).
        hashed_password (str): The hashed password (non-nullable).
        session_id (str): The session ID (nullable).
        reset_token (str): The reset token (nullable).
    """
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str, session_id: str = None, reset_token: str = None):
        """
        Initialize a User instance.
        Args:
            email (str): The user's email.
            hashed_password (str): The hashed password.
            session_id (str, optional): The session ID.
            reset_token (str, optional): The reset token.
        """
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token
