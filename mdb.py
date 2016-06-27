##Courtesy:  http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php \
##and the next articles in the series

from pymongo import MongoClient

def establish_connection():
	
	connection = MongoClient("localhost:27017")
	# MongoDB URI format:MongoClient('mongodb://localhost:27017/')

	#print all the existing databases:
	print connection.database_names()

	db = connection.myFirstMB #accessing the db, similar to use <db>
	return db
	

def insert_data(db, value):
	
	db.countries.insert(value)
	#db.countries.insert({"name" : "USA"})
	#db.countries.insert({"name" : "Poland"})

def get_first_data(db): 
	 
	 return db.countries.find_one() # return the first row/document  in the collection 

def get_all(db):
	
	for value in db.countries.find():
		print value

def number_of_records(db):
		
		return db.countries.count()

def find_country_count(db, user_country):
	
	for value in db.countries.find({'name':user_country}):
		print value

	print "The number of required records are %d" %db.countries.find({'name':user_country}).count()

if __name__ == "__main__":
	
	try:
		db = establish_connection()
		print db.collection_names() #print the list of collections
		print "countries" in db.collection_names() #check if the collection called countries exists in the db or not

		# record_id=insert_data(db,{"name" : "Germany"})
		# print record_id
		# record_id=insert_data(db,{"name" : "India"})
		# print record_id
		print "First Data is %s "%get_first_data(db)
		print "All Data is ---"
		get_all(db)
		print "--The number of documents in the collection are %d "%number_of_records(db)
		user_country = raw_input("Enter the country you wish to find ::  ")
		find_country_count(db,user_country)

	except Exception, e:
		raise e
	
