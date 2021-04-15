class User(BaseModel):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)