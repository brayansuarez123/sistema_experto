import os

DATABASE_NAME = os.environ.get("DATABASE_NAME", "movie_expert")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "expert")
DATABASE_USER = os.environ.get("DATABASE_USER", "expert")