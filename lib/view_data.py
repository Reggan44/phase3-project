from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Director, Genre, Actor, Movie

engine = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=engine)
session = Session()

# see all movies
movies = session.query(Movie).all()
for movie in movies:
    print(f"Title: {movie.title}, Year: {movie.year}, Director: {movie.director.name}, Genre: {movie.genre.name}")
    print("Actors:", ", ".join(actor.name for actor in movie.actors))
    print("-" * 40)