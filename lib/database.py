from sqlalchemy import create_engine
from lib.models import Base
# Create a SQLite database called 'movies.db'
engine = create_engine('sqlite:///movies.db')

Base.metadata.create_all(engine)

print("Database and tables created!") 