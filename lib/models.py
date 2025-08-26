
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

# Association table for many-to-many relationship between Movie and Actor
movie_actor = Table(
	'movie_actor', Base.metadata,
	Column('movie_id', Integer, ForeignKey('movies.id')),
	Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(Base):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key=True)
	title = Column(String, nullable=False)
	year = Column(Integer)
	director_id = Column(Integer, ForeignKey('directors.id'))
	genre_id = Column(Integer, ForeignKey('genres.id'))
	director = relationship('Director', back_populates='movies')
	genre = relationship('Genre', back_populates='movies')
	actors = relationship('Actor', secondary=movie_actor, back_populates='movies')


class Director(Base):
	__tablename__ = 'directors'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	movies = relationship('Movie', back_populates='director')


class Genre(Base):
	__tablename__ = 'genres'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	movies = relationship('Movie', back_populates='genre')

class Actor(Base):
	__tablename__ = 'actors'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	movies = relationship('Movie', secondary=movie_actor, back_populates='actors')
