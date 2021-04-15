from sqlalchemy import Column, DateTime, String, Integer, ForeignKey

class BaseModel(db.Model):
# cxz"""Base data model for all objects"""
__abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models