import sqlite3
from sqlite3 import Error
import time


def generate_key(word1, word2):
	key_length=len(word2)
	start_char=word1
	end_char=word2
	alphabets="abcdefghijklmnopqrstuvwxyz"

	temp=[]
	range_query=[]
	final_keys=[]
	start_time=time.time()
	for i in range(0,26):
	    if    ord(alphabets[i]) < ord(start_char[0]) :
	        continue
	    if  ord(alphabets[i]) > ord(end_char[0]):
	        break
	    temp.append(alphabets[i])

	for p in range(1,key_length+1):
	    range_query=temp
	    temp=[]   
	    # print(range_query)
	    for j in range(len(range_query)):
	        for i in range(0,26):
	            temp_word=range_query[j]+alphabets[i]
	            if temp_word >= start_char[:len(temp_word)] and temp_word <= end_char[:len(temp_word)]:
	                temp.append(temp_word)
	    
	end_time=time.time()
	# print("keys ", range_query)
	# print("No. of keys ", len(range_query))
	print("time taken for key generation", end_time -start_time)
	return range_query
    




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
	word1 = input("Enter word1: ")
	word2 = input("Enter word2: ")

	#Generate keys for the given input
	keys = generate_key(word1,word2)
	# print("Keys are",keys)



	database0 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite.db"
	database1 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite1.db"
	database2 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite2.db"
	database3 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite3.db"



	start_time = time.time()
	# create a database connection
	conn = create_connection(database0)

	# create tables
	if conn is not None:
		# create projects table
		# create_table(conn, sql_create_projects_table)
		try:
			
			c = conn.cursor()
			fetch_query = "SELECT * FROM Words where word IN ("
			# print(type(keys[0]))
			for key in keys:
				fetch_query = fetch_query + "'" +key+"'" + "," 
			fetch_query = fetch_query[:-1] + ")"
			# print(fetch_query)
			print(c.execute(fetch_query))
			print("The results fetched from database 1 for key " + key + " are:")
			print(c.fetchall())
			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")



	# create a database connection
	conn = create_connection(database1)

	# create tables
	if conn is not None:
		# create projects table
		# create_table(conn, sql_create_projects_table)
		try:
			
			c = conn.cursor()
			fetch_query = "SELECT * FROM Words where word IN ("
			# print(type(keys[0]))
			for key in keys:
				fetch_query = fetch_query + "'" +key+"'" + "," 
			fetch_query = fetch_query[:-1] + ")"
			# print(fetch_query)
			c.execute(fetch_query)
			print("The results fetched from database 2 for key " + key + " are:")
			print(c.fetchall())
			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")


	# create a database connection
	conn = create_connection(database2)

	# create tables
	if conn is not None:
		# create projects table
		# create_table(conn, sql_create_projects_table)
		try:
			
			c = conn.cursor()
			fetch_query = "SELECT * FROM Words where word IN ("
			# print(type(keys[0]))
			for key in keys:
				fetch_query = fetch_query + "'" +key+"'" + "," 
			fetch_query = fetch_query[:-1] + ")"
			# print(fetch_query)
			c.execute(fetch_query)
			print("The results fetched from database 3 for key " + key + " are:")
			print(c.fetchall())
			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")


	# create a database connection
	conn = create_connection(database3)

	# create tables
	if conn is not None:
		# create projects table
		# create_table(conn, sql_create_projects_table)
		try:
			
			c = conn.cursor()
			fetch_query = "SELECT * FROM Words where word IN ("
			# print(type(keys[0]))
			for key in keys:
				fetch_query = fetch_query + "'" +key+"'" + "," 
			fetch_query = fetch_query[:-1] + ")"
			# print(fetch_query)
			c.execute(fetch_query)
			print("The results fetched from database 4 for key " + key + " are:")
			print(c.fetchall())
			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")
	end_time = time.time()


	print("Total Time taken to process the query: ", end_time-start_time)

if __name__ == '__main__':
	main()

