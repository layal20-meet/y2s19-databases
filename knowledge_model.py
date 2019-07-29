from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='Knowledge'
	article_id=Column(Integer, primary_key=True)
	topic=Column(String)
	title=Column(String)
	rating=Column(Integer)
	
	def __repr__(self):
		return (
			"ID:{}"
			"the topic is: {}\n"
			"the title is: {}\n"
			"the rating is: {}\n").format(
				self.article_id,
				self.topic,
				self.title,
				self.rating)
	