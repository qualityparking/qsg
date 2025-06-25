from app import db
from sqlalchemy import Column, Integer, String, Enum
import enum

class RoleEnum(enum.Enum):
    admin = 'admin'
    operator = 'operator'
    member = 'member'

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
