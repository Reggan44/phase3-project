from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Movie, Director, Genre, Actor, Base
import lib.helpers as helpers

engine = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=engine)
session = Session()

def main():
	while True:
		print("\nPlease select an option:")
		print("0. Exit the program")
		print("1. List all movies")
		print("2. Find movie by title")
		print("3. Find movie by id")
		print("4. Create movie")
		print("5. Update movie")
		print("6. Delete movie")
		print("7. List all directors")
		print("8. Find director by name")
		print("9. Find director by id")
		print("10. Create director")
		print("11. Update director")
		print("12. Delete director")
		print("13. List all genres")
		print("14. Find genre by name")
		print("15. Find genre by id")
		print("16. Create genre")
		print("17. Update genre")
		print("18. Delete genre")
		print("19. List all actors")
		print("20. Find actor by name")
		print("21. Find actor by id")
		print("22. Create actor")
		print("23. Update actor")
		print("24. Delete actor")
		choice = input("> ")

		if choice == "0":
			print("Goodbye!")
			break
		elif choice == "1":
			movies = helpers.get_all_movies(session)
			for m in movies:
				print(f"{m.id}: {m.title} ({m.year}) - Director: {m.director.name}, Genre: {m.genre.name}, Actors: {', '.join(a.name for a in m.actors)}")
		elif choice == "2":
			title = input("Enter movie title: ")
			movies = session.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()
			for m in movies:
				print(f"{m.id}: {m.title} ({m.year})")
		elif choice == "3":
			movie_id = int(input("Enter movie id: "))
			movie = session.query(Movie).get(movie_id)
			if movie:
				print(f"{movie.id}: {movie.title} ({movie.year})")
			else:
				print("Movie not found.")
		elif choice == "4":
			title = input("Title: ")
			year = int(input("Year: "))
			director_id = int(input("Director id: "))
			genre_id = int(input("Genre id: "))
			actor_ids = input("Actor ids (space separated): ").split()
			director = session.query(Director).get(director_id)
			genre = session.query(Genre).get(genre_id)
			actors = session.query(Actor).filter(Actor.id.in_([int(i) for i in actor_ids])).all()
			movie = helpers.create_movie(session, title, year, director, genre, actors)
			print(f"Created movie: {movie.title}")
		elif choice == "5":
			movie_id = int(input("Movie id: "))
			title = input("New title (leave blank to keep current): ") or None
			year = input("New year (leave blank to keep current): ")
			year = int(year) if year else None
			director_id = input("New director id (leave blank to keep current): ")
			director = session.query(Director).get(int(director_id)) if director_id else None
			genre_id = input("New genre id (leave blank to keep current): ")
			genre = session.query(Genre).get(int(genre_id)) if genre_id else None
			actor_ids = input("New actor ids (space separated, leave blank to keep current): ")
			actors = session.query(Actor).filter(Actor.id.in_([int(i) for i in actor_ids.split()])) if actor_ids else None
			movie = helpers.update_movie(session, movie_id, title, year, director, genre, actors)
			print(f"Updated movie: {movie.title if movie else 'Not found'}")
		elif choice == "6":
			movie_id = int(input("Movie id: "))
			success = helpers.delete_movie(session, movie_id)
			print("Deleted movie" if success else "Movie not found")
		elif choice == "7":
			directors = helpers.get_all_directors(session)
			for d in directors:
				print(f"{d.id}: {d.name}")
		elif choice == "8":
			name = input("Enter director name: ")
			directors = session.query(Director).filter(Director.name.ilike(f"%{name}%")).all()
			for d in directors:
				print(f"{d.id}: {d.name}")
		elif choice == "9":
			director_id = int(input("Enter director id: "))
			director = session.query(Director).get(director_id)
			if director:
				print(f"{director.id}: {director.name}")
			else:
				print("Director not found.")
		elif choice == "10":
			name = input("Director name: ")
			director = helpers.create_director(session, name)
			print(f"Created director: {director.name}")
		elif choice == "11":
			director_id = int(input("Director id: "))
			name = input("New name: ")
			director = helpers.update_director(session, director_id, name)
			print(f"Updated director: {director.name if director else 'Not found'}")
		elif choice == "12":
			director_id = int(input("Director id: "))
			success = helpers.delete_director(session, director_id)
			print("Deleted director" if success else "Director not found")
		elif choice == "13":
			genres = helpers.get_all_genres(session)
			for g in genres:
				print(f"{g.id}: {g.name}")
		elif choice == "14":
			name = input("Enter genre name: ")
			genres = session.query(Genre).filter(Genre.name.ilike(f"%{name}%")).all()
			for g in genres:
				print(f"{g.id}: {g.name}")
		elif choice == "15":
			genre_id = int(input("Enter genre id: "))
			genre = session.query(Genre).get(genre_id)
			if genre:
				print(f"{genre.id}: {genre.name}")
			else:
				print("Genre not found.")
		elif choice == "16":
			name = input("Genre name: ")
			genre = helpers.create_genre(session, name)
			print(f"Created genre: {genre.name}")
		elif choice == "17":
			genre_id = int(input("Genre id: "))
			name = input("New name: ")
			genre = helpers.update_genre(session, genre_id, name)
			print(f"Updated genre: {genre.name if genre else 'Not found'}")
		elif choice == "18":
			genre_id = int(input("Genre id: "))
			success = helpers.delete_genre(session, genre_id)
			print("Deleted genre" if success else "Genre not found")
		elif choice == "19":
			actors = helpers.get_all_actors(session)
			for a in actors:
				print(f"{a.id}: {a.name}")
		elif choice == "20":
			name = input("Enter actor name: ")
			actors = session.query(Actor).filter(Actor.name.ilike(f"%{name}%")).all()
			for a in actors:
				print(f"{a.id}: {a.name}")
		elif choice == "21":
			actor_id = int(input("Enter actor id: "))
			actor = session.query(Actor).get(actor_id)
			if actor:
				print(f"{actor.id}: {actor.name}")
			else:
				print("Actor not found.")
		elif choice == "22":
			name = input("Actor name: ")
			actor = helpers.create_actor(session, name)
			print(f"Created actor: {actor.name}")
		elif choice == "23":
			actor_id = int(input("Actor id: "))
			name = input("New name: ")
			actor = helpers.update_actor(session, actor_id, name)
			print(f"Updated actor: {actor.name if actor else 'Not found'}")
		elif choice == "24":
			actor_id = int(input("Actor id: "))
			success = helpers.delete_actor(session, actor_id)
			print("Deleted actor" if success else "Actor not found")
		else:
			print("Invalid option. Please try again.")

if __name__ == "__main__":
	main()
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Director, Genre, Actor, Movie
import lib.helpers as helpers

engine = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=engine)
session = Session()

def main():
	parser = argparse.ArgumentParser(description='Movie App CLI')
	subparsers = parser.add_subparsers(dest='command')

	# Movie commands
	movie_parser = subparsers.add_parser('movie')
	movie_sub = movie_parser.add_subparsers(dest='action')

	movie_add = movie_sub.add_parser('add')
	movie_add.add_argument('--title', required=True)
	movie_add.add_argument('--year', type=int, required=True)
	movie_add.add_argument('--director_id', type=int, required=True)
	movie_add.add_argument('--genre_id', type=int, required=True)
	movie_add.add_argument('--actor_ids', nargs='+', type=int, required=True)

	movie_list = movie_sub.add_parser('list')

	movie_update = movie_sub.add_parser('update')
	movie_update.add_argument('--id', type=int, required=True)
	movie_update.add_argument('--title')
	movie_update.add_argument('--year', type=int)
	movie_update.add_argument('--director_id', type=int)
	movie_update.add_argument('--genre_id', type=int)
	movie_update.add_argument('--actor_ids', nargs='+', type=int)

	movie_delete = movie_sub.add_parser('delete')
	movie_delete.add_argument('--id', type=int, required=True)

	# Director commands
	director_parser = subparsers.add_parser('director')
	director_sub = director_parser.add_subparsers(dest='action')

	director_add = director_sub.add_parser('add')
	director_add.add_argument('--name', required=True)

	director_list = director_sub.add_parser('list')

	director_update = director_sub.add_parser('update')
	director_update.add_argument('--id', type=int, required=True)
	director_update.add_argument('--name')

	director_delete = director_sub.add_parser('delete')
	director_delete.add_argument('--id', type=int, required=True)

	# Genre commands
	genre_parser = subparsers.add_parser('genre')
	genre_sub = genre_parser.add_subparsers(dest='action')

	genre_add = genre_sub.add_parser('add')
	genre_add.add_argument('--name', required=True)

	genre_list = genre_sub.add_parser('list')

	genre_update = genre_sub.add_parser('update')
	genre_update.add_argument('--id', type=int, required=True)
	genre_update.add_argument('--name')

	genre_delete = genre_sub.add_parser('delete')
	genre_delete.add_argument('--id', type=int, required=True)

	# Actor commands
	actor_parser = subparsers.add_parser('actor')
	actor_sub = actor_parser.add_subparsers(dest='action')

	actor_add = actor_sub.add_parser('add')
	actor_add.add_argument('--name', required=True)

	actor_list = actor_sub.add_parser('list')

	actor_update = actor_sub.add_parser('update')
	actor_update.add_argument('--id', type=int, required=True)
	actor_update.add_argument('--name')

	actor_delete = actor_sub.add_parser('delete')
	actor_delete.add_argument('--id', type=int, required=True)

	args = parser.parse_args()

	if args.command == 'movie':
		if args.action == 'add':
			director = session.query(Director).get(args.director_id)
			genre = session.query(Genre).get(args.genre_id)
			actors = session.query(Actor).filter(Actor.id.in_(args.actor_ids)).all()
			movie = helpers.create_movie(session, args.title, args.year, director, genre, actors)
			print(f"Added movie: {movie.title}")
		elif args.action == 'list':
			movies = helpers.get_all_movies(session)
			for m in movies:
				print(f"{m.id}: {m.title} ({m.year}) - Director: {m.director.name}, Genre: {m.genre.name}, Actors: {', '.join(a.name for a in m.actors)}")
		elif args.action == 'update':
			director = session.query(Director).get(args.director_id) if args.director_id else None
			genre = session.query(Genre).get(args.genre_id) if args.genre_id else None
			actors = session.query(Actor).filter(Actor.id.in_(args.actor_ids)).all() if args.actor_ids else None
			movie = helpers.update_movie(session, args.id, args.title, args.year, director, genre, actors)
			print(f"Updated movie: {movie.title if movie else 'Not found'}")
		elif args.action == 'delete':
			success = helpers.delete_movie(session, args.id)
			print("Deleted movie" if success else "Movie not found")

	elif args.command == 'director':
		if args.action == 'add':
			director = helpers.create_director(session, args.name)
			print(f"Added director: {director.name}")
		elif args.action == 'list':
			directors = helpers.get_all_directors(session)
			for d in directors:
				print(f"{d.id}: {d.name}")
		elif args.action == 'update':
			director = helpers.update_director(session, args.id, args.name)
			print(f"Updated director: {director.name if director else 'Not found'}")
		elif args.action == 'delete':
			success = helpers.delete_director(session, args.id)
			print("Deleted director" if success else "Director not found")

	elif args.command == 'genre':
		if args.action == 'add':
			genre = helpers.create_genre(session, args.name)
			print(f"Added genre: {genre.name}")
		elif args.action == 'list':
			genres = helpers.get_all_genres(session)
			for g in genres:
				print(f"{g.id}: {g.name}")
		elif args.action == 'update':
			genre = helpers.update_genre(session, args.id, args.name)
			print(f"Updated genre: {genre.name if genre else 'Not found'}")
		elif args.action == 'delete':
			success = helpers.delete_genre(session, args.id)
			print("Deleted genre" if success else "Genre not found")

	elif args.command == 'actor':
		if args.action == 'add':
			actor = helpers.create_actor(session, args.name)
			print(f"Added actor: {actor.name}")
		elif args.action == 'list':
			actors = helpers.get_all_actors(session)
			for a in actors:
				print(f"{a.id}: {a.name}")
		elif args.action == 'update':
			actor = helpers.update_actor(session, args.id, args.name)
			print(f"Updated actor: {actor.name if actor else 'Not found'}")
		elif args.action == 'delete':
			success = helpers.delete_actor(session, args.id)
			print("Deleted actor" if success else "Actor not found")

if __name__ == '__main__':
	main()
