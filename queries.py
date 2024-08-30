import sqlite3

def main():
    """
    Main function to connect to the database and display
    the number of directors.
    """
    try:
        conn = sqlite3.connect('data/movies.sqlite')
        db = conn.cursor()

        print("Number of directors:", directors_count(db))

    finally:
        conn.close()

def directors_count(db):
    """
    Returns the total number of directors in the database.

    Args:
        db: SQLite cursor object.

    Returns:
        int: Number of directors.
    """
    query = "SELECT CAST(COUNT(name) AS INTEGER) FROM directors"
    db.execute(query)
    return db.fetchone()[0]

def directors_list(db):
    """
    Returns a sorted list of director names.

    Args:
        db: SQLite cursor object.

    Returns:
        list: List of director names in alphabetical order.
    """
    query = "SELECT name FROM directors ORDER BY name ASC;"
    db.execute(query)
    result = db.fetchall()
    return [name[0] for name in result]

def river_movies(db):
    """
    Returns a list of movie titles containing the word 'River'.

    Args:
        db: SQLite cursor object.

    Returns:
        list: List of movie titles that contain 'River'.
    """
    query = """
    SELECT title
    FROM movies
    WHERE title LIKE '% River %'  -- 'River' in the middle of the title
    OR title LIKE 'River %'       -- 'River' at the start of the title
    OR title LIKE '% River'       -- 'River' at the end of the title
    OR title = 'River'            -- The title is exactly 'River'
    ORDER BY title ASC;
    """
    db.execute(query)
    result = db.fetchall()
    return [title[0] for title in result]

def directors_named_like_count(db, name):
    """
    Returns the count of directors whose names contain a specified string.

    Args:
        db: SQLite cursor object.
        name (str): The string to search for in director names.

    Returns:
        int: Number of directors whose names match the search criteria.
    """
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?;"
    db.execute(query, ('%' + name + '%',))
    return db.fetchone()[0]

def movies_longer_than(db, min_length):
    """
    Returns a list of movie titles that are longer than a specified length.

    Args:
        db: SQLite cursor object.
        min_length (int): The minimum movie length in minutes.

    Returns:
        list: List of movie titles longer than the specified length.
    """
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC;"
    db.execute(query, (min_length,))
    result = db.fetchall()
    return [title[0] for title in result]

if __name__ == "__main__":
    main()
