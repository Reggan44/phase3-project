from lib.models import Movie, Director, Genre, Actor

# Movie CRUD
def create_movie(session, title, year, director, genre, actors):
	movie = Movie(title=title, year=year, director=director, genre=genre, actors=actors)
	session.add(movie)
	session.commit()
	return movie

def get_all_movies(session):
	return session.query(Movie).all()

def update_movie(session, movie_id, title=None, year=None, director=None, genre=None, actors=None):
	movie = session.query(Movie).get(movie_id)
	if movie:
		if title is not None:
			movie.title = title
		if year is not None:
			movie.year = year
		if director is not None:
			movie.director = director
		if genre is not None:
			movie.genre = genre
		if actors is not None:
			movie.actors = actors
		session.commit()
	return movie

def delete_movie(session, movie_id):
	movie = session.query(Movie).get(movie_id)
	if movie:
		session.delete(movie)
		session.commit()
		return True
	return False

# Director CRUD
def create_director(session, name):
	director = Director(name=name)
	session.add(director)
	session.commit()
	return director

def get_all_directors(session):
	return session.query(Director).all()

def update_director(session, director_id, name=None):
	director = session.query(Director).get(director_id)
	if director and name is not None:
		director.name = name
		session.commit()
	return director

def delete_director(session, director_id):
	director = session.query(Director).get(director_id)
	if director:
		session.delete(director)
		session.commit()
		return True
	return False

# Genre CRUD
def create_genre(session, name):
	genre = Genre(name=name)
	session.add(genre)
	session.commit()
	return genre

def get_all_genres(session):
	return session.query(Genre).all()

def update_genre(session, genre_id, name=None):
	genre = session.query(Genre).get(genre_id)
	if genre and name is not None:
		genre.name = name
		session.commit()
	return genre

def delete_genre(session, genre_id):
	genre = session.query(Genre).get(genre_id)
	if genre:
		session.delete(genre)
		session.commit()
		return True
	return False

# Actor CRUD
def create_actor(session, name):
	actor = Actor(name=name)
	session.add(actor)
	session.commit()
	return actor

def get_all_actors(session):
	return session.query(Actor).all()

def update_actor(session, actor_id, name=None):
	actor = session.query(Actor).get(actor_id)
	if actor and name is not None:
		actor.name = name
		session.commit()
	return actor

def delete_actor(session, actor_id):
	actor = session.query(Actor).get(actor_id)
	if actor:
		session.delete(actor)
		session.commit()
		return True
	return False
