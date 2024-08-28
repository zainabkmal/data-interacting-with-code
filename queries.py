import sqlite3

def directors_count(db):
    query = "SELECT CAST(COUNT(name) AS INTEGER) FROM directors"
    db.execute(query)
    result = db.fetchall()
    return result[0][0]



def directors_list(db):
    query = "SELECT name FROM directors ORDER BY name ASC;"
    db.execute(query)
    result = db.fetchall()
    return [name[0] for name in result]



def river_movies(db):
    # Use word boundaries to ensure "river" is matched as a whole word, not as a substring
    query = """
        SELECT title
        FROM movies
        WHERE title LIKE '% River %'  -- 'River' in the middle of the title
        OR title LIKE 'River %'       -- 'River' at the start of the title
        OR title LIKE '% River'       -- 'River' at the end of the title
        OR title = 'River'            -- The title is exactly 'River'
        ORDER BY title ASC; """
    db.execute(query)
    result = db.fetchall()
    return [title[0] for title in result]




def directors_named_like_count(db, name):
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?;"
    db.execute(query, ('%' + name + '%',))
    result = db.fetchone()
    return result[0]



def movies_longer_than(db, min_length):
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC;"
    db.execute(query, (min_length,))
    result = db.fetchall()
    return [title[0] for title in result]



# Main part of the program
def main():
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()

    print("Number of directors:", directors_count(db))

    conn.close()
