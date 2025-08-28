from sqlalchemy import create_engine
from lib.db.models import Base
# make a db called 'movies.db'
engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)
print("Database and tables created!")