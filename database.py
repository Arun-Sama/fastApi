from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

data_url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/testdb"

engine = create_engine(data_url)

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = "Details"
    name = Column(String(250), primary_key=True)
    price = Column(Integer)
    Brand = Column(String(250))


Base.metadata.create_all(bind=engine)
