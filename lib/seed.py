


from lib.models import Director, Genre, Actor, Movie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker






# add a SQLite database called 'movies.db'
engine = create_engine('sqlite:///movies.db')

# add tables
Base.metadata.create_all(engine)

# add a session
Session = sessionmaker(bind=engine)
session = Session()

# add directors

# add directors
director1 = Director(name="Steven Spielberg")
director2 = Director(name="Christopher Nolan")

# add genres
genre1 = Genre(name="Adventure")
genre2 = Genre(name="Sci-Fi")

# add actors
actor1 = Actor(name="Tom Hanks")
actor2 = Actor(name="Leonardo DiCaprio")
actor3 = Actor(name="Morgan Freeman")

# imput movies
movie1 = Movie(
	title="Jurassic Park",
	year=1993,
	director=director1,
	genre=genre1,
	actors=[actor1, actor3]
)
movie2 = Movie(
	title="Inception",
	year=2010,
	director=director2,
	genre=genre2,
	actors=[actor2]
)

session.add_all([
	director1, director2,
	genre1, genre2,
	actor1, actor2, actor3,
	movie1, movie2
])
session.commit()

print("Sample data added!")