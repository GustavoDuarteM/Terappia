from config.database import db
from flask_sqlalchemy import SQLAlchemy

Base = database.db.Model
 
class BaseModel(Base):
# cxz"""Base data model for all objects"""
__abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models