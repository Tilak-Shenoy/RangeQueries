import sqlite3
from sqlite3 import Error
import time


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
	database0 = r"/home/tilak/Dev/RangeQueries/pythonsqlite.db"
	database1 = r"/home/tilak/Dev/RangeQueries/pythonsqlite1.db"
	database2 = r"/home/tilak/Dev/RangeQueries/pythonsqlite2.db"
	database3 = r"/home/tilak/Dev/RangeQueries/pythonsqlite3.db"



	start_time = time.time()
	# create a database connection
	conn = create_connection(database1)

	# create tables
	if conn is not None:
		# create projects table
		# create_table(conn, sql_create_projects_table)
		try:
			
			c = conn.cursor()
		
			fetch_query = """SELECT * FROM Words;"""
			c.execute(fetch_query)
			# print("The results fetched from database 1 for key " + key + " are:")
			print(c.fetchall(), end = '\n')
			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")


if __name__ == '__main__':
	main()