import sqlite3
from sqlite3 import Error
import time
import _thread
import threading

class myThread (threading.Thread):
	def __init__(self, threadID, name, database, keys):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.database = database
		self.keys = keys
	def run(self):
		runQuery(self.database, self.keys)


def generate_key(word1, word2, length):
	key_length=length
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


def runQuery(database, keys):
	conn = create_connection(database)
	databaseName = database.split("/")

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
			print("The results fetched from" + databaseName[-1] + " for key " + key + " are:", c.fetchall())

			conn.commit()
			conn.close()
		except Error as e:
			print(e)
	else:
		print("Error! cannot create the database connection.")


def main():
	word1 = input("Enter word1: ")
	word2 = input("Enter word2: ")
	le = int(input("Enter key length: "))
	#Generate keys for the given input
	keys = generate_key(word1,word2,le)
	# print("Keys are",keys)



	database0 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite.db"
	database1 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite1.db"
	database2 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite2.db"
	database3 = r"/Users/gaurav/Documents/coding/adbms/project/pythonsqlite3.db"



	start_time = time.time()
	thread1 = myThread(1, "Thread-1", database0, keys)
	thread2 = myThread(2, "Thread-2", database1, keys)
	thread3 = myThread(2, "Thread-2", database1, keys)
	thread4 = myThread(2, "Thread-2", database1, keys)
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	end_time = time.time()
	print("Total Time taken to process the query using multithreading: ", end_time-start_time)
	start_time = time.time()
	runQuery(database0, keys)
	runQuery(database1, keys)
	runQuery(database2, keys)
	runQuery(database3, keys)

	# try:
	#    t1 = _thread.start_new_thread( runQuery, (database0, keys, ) )
	#    t2 = _thread.start_new_thread( runQuery, (database1, keys, ) )
	# except:
	# 	print("Error: unable to start thread")
	end_time = time.time()
	print("Total Time taken to process the query: ", end_time-start_time)

if __name__ == '__main__':
	main()

