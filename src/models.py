import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    nickname = Column(String(50), nullable = False)
    email = Column(String(100), nullable = False)
    password = Column(String(500), nullable = False)
    follower = relationship("follower")
    comment = relationship("comment")
    post = relationship("post")




class Follower(Base):
    __tablename__ = "follower"
    
    id = Column(Integer, primary_key = True)
    user_follow_from_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    user_follow_to_id = Column(Integer, nullable = False)


class Post(Base): 
    __tablename__ = "post"

    id = Column(Integer, primary_key = True)
    description = Column(String(120), nullable = False)
    image_url = Column(String(300), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)



class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key = True)
    comment_text = Column(String(180), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    


    

    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
