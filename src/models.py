import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_ID = Column(Integer, primary_key=True)
    username = Column(String(20))
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    char_ID = Column(Integer, primary_key=True)
    char_name = Column(String(50), nullable=False )
    dimension = Column(String(250), nullable=True)
    origin = Column(String(250), nullable=False)
    status = Column(String(10), nullable=False)


class Episodes(Base):
    __tablename__ = 'episodes'
    Ep_ID = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False )
    Air_Date = Column(String(250), nullable=False)
    


class Ep_Favorites(Base):
    __tablename__ = 'ep_favorites'
    fav_ep_id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey ("user.user_ID"))
    ep_ID = Column(Integer, ForeignKey ("episodes.ep_ID"))
    rel = relationship(Episodes)
    rel= relationship (Characters)

class Char_Favorites(Base):
    __tablename__ = 'char_favorites'
    fav_char_id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey("user.user_ID"))
    char_ID = Column(Integer, ForeignKey("characters.char_ID"))

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')