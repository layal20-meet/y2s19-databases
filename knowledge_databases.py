from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	topic_object=Knowledge(
		topic = topic,
		title = title,
		rating = rating)
	session.add(topic_object)
	session.commit()

add_article("food", "chocolate", 10)
add_article("dance", "ballet", 9)
add_article("students", "layal", 8)


def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return(knowledge)

print(query_all_articles())

def query_article_by_topic(new_topic):
	knowledge = session.query(Knowledge).filter_by(topic=new_topic)
	return(knowledge)

def delete_article_by_topic(new_topic):
	session.query(Knowledge).filter_by(topic=new_topic).delete()
	session.commit()
delete_article_by_topic("food")

def delete_all_articles():
	knowledge=session.query(Knowledge).delete_all()
	session.commit()

def edit_article_rating(new_rating):
	Knowledge_object = session.query(
       Knowledge).filter_by(
       rating=new_rating).first()
	Knowledge_object.rating = new_rating
	session.commit()

