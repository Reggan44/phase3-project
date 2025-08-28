


from lib.db.models import Director, Genre, Actor, Movie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker






# make a db called 'movies.db'
engine = create_engine('sqlite:///movies.db')

# make tables
Base.metadata.create_all(engine)

# make a session
Session = sessionmaker(bind=engine)
session = Session()

# put directors

# put directors
director1 = Director(name="Steven Spielberg")
director2 = Director(name="Christopher Nolan")

# put genres
genre1 = Genre(name="Adventure")
genre2 = Genre(name="Sci-Fi")

# put actors
actor1 = Actor(name="Tom Hanks")
actor2 = Actor(name="Leonardo DiCaprio")
actor3 = Actor(name="Morgan Freeman")

# put movies (imput lol)
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

print("data added!")