from pymongo import MongoClient

def establish_connection():
	connection=MongoClient("localhost:27017")
	db=connection.stores
	return db

def insert_data(db):
	db.stores.insert([
    { '_id': 1, 'name': "Java Hut", 'description': "Coffee and cakes" },
    { '_id': 2, 'name': "Burger Buns", 'description': "Gourmet hamburgers" },
    { '_id': 3, 'name': "Coffee Shop", 'description': "Just coffee" },
    { '_id': 4, 'name': "Clothes Clothes Clothes", 'description': "Discount clothing" },
    { '_id': 5, 'name': "Java Shopping", 'description': "Indonesian goods" },
    { '_id': 6, 'name': "Java", 'description': "Koreain Tea" }
   ])


def create_text_index(db):
	db.stores.create_index([('name', "text"), ('description', "text")])

def perform_text_query(db):
	#Will print all the rows that have either java, coffee or shop in them. 
	for i in db.stores.find({'$text': {'$search': "java coffee shop"}}):
		print i

def exact_query(db):
	#find where search term is coffee shop or only java
	for i in db.stores.find({'$text': {'$search': "Java \"coffee shop\"" }}):
		print i

def term_exlusion(db):
	for i in db.stores.find({'$text': {'$search': "java shop -coffee"}}):
		print i

if __name__=="__main__":
	try:
		db=establish_connection()
		insert_data(db)
		#print "1"
		create_text_index(db)
		#print db.stores.getIndexes()
		#print "2"
		print "\n\nThe result of query java coffee shop is:"
		perform_text_query(db)
		#print "3"
		print "\n\nThe result of query either java or \"coffee shop\" is:"
		exact_query(db)
		print "\n\nThe result of query either java or shop but not coffee is:"
		term_exlusion(db)
		db.stores.drop()

	except Exception, e:
		raise e	