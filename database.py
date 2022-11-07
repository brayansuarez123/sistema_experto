import mysql.connector
from config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER

db = mysql.connector.connect(
    host=DATABASE_HOST,
    database=DATABASE_NAME,
    password=DATABASE_PASSWORD,
    user=DATABASE_USER,
)

__all__ = ["db"]
