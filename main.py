import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query = """
        DROP TABLE animal_type
    """
    #     CREATE TABLE colors (
    #         id integer PRIMARY KEY AUTOINCREMENT,
    #         name varchar(30)
    #     )
    # """

    cursor.execute(query)