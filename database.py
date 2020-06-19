import sqlite3
from sqlite3 import Error
from nltk.corpus import words
import random

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def main():
    database = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite3.db"

    listOfWords = words.words()
    random.seed(4)

    random.shuffle(listOfWords)
    listOfWords = list(set(listOfWords[177504:]))

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        # create_table(conn, sql_create_projects_table)
        try:
            
            c = conn.cursor()
            for word in listOfWords:

                insert_query = """INSERT INTO words (word)
                              VALUES(?);
                            """
                c.execute(insert_query,(word,))
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
        # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
