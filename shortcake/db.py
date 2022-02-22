"""Database connection file.

    Query PostgreSQL db to check db version.
"""

import psycopg2

def connect():
    """Connect to PostgreSQL db and query for db version."""
    connection = None

    # Connect to db
    connection = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "postgres",
        port = "5432")

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Execute query
        cursor.execute("SELECT VERSION();")
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated.")

if __name__ == "__main__":
    connect()
