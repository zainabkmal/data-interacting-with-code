"""
Module for executing various SQL queries on a movie database.
Provides functions to retrieve information about directors and movies.
"""
import sqlite3

def directors_count(db_instance):
    """
    Returns the count of directors in the database.
    :param database_cursor: SQLite cursor object.
    :return: Integer representing the number of directors.
    """
    query = "SELECT CAST(COUNT(name) AS INTEGER) FROM directors"
    db_instance.execute(query)
    result = db_instance.fetchall()
    return result[0][0]


def directors_list(db_instance):
    """
    Returns a list of director names sorted alphabetically.
    :param database_cursor: SQLite cursor object.
    :return: List of director names.
    """
    query = "SELECT name FROM directors ORDER BY name ASC;"
    db_instance.execute(query)
    result = db_instance.fetchall()
    return [name[0] for name in result]

def river_movies(db_instance):
    """
    Returns a list of movie titles containing the word 'River'.
    :param database_cursor: SQLite cursor object.
    :return: List of movie titles.
    """
    query = """
    SELECT title
    FROM movies
    WHERE title LIKE '% River %'  -- 'River' in the middle of the title
    OR title LIKE 'River %'       -- 'River' at the start of the title
    OR title LIKE '% River'       -- 'River' at the end of the title
    OR title = 'River'            -- The title is exactly 'River'
    ORDER BY title ASC; """
    db_instance.execute(query)
    result = db_instance.fetchall()
    return [title[0] for title in result]


def directors_named_like_count(db_instance, name):
    """
    Returns the count of directors whose names contain a specified substring.
    :param database_cursor: SQLite cursor object.
    :param name: Substring to search for in director names.
    :return: Integer count of matching directors.
    """
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?;"
    db_instance.execute(query, ('%' + name + '%',))
    result = db_instance.fetchone()
    return result[0]


def movies_longer_than(db_instance, min_length):
    """
    Returns a list of movie titles longer than a specified length.
    :param database_cursor: SQLite cursor object.
    :param min_length: Minimum length of movies in minutes.
    :return: List of movie titles.
    """
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC;"
    db_instance.execute(query, (min_length,))
    result = db_instance.fetchall()
    return [title[0] for title in result]


def main():
    """
    Main function to connect to the SQLite database, execute queries,
    and display results.
    """
    conn = sqlite3.connect('data/movies.sqlite')
    db_instance = conn.cursor()
    print("Number of directors:", directors_count(db_instance))
    conn.close()
