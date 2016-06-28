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
	db.stores.create_index([('name',"text"), ('description',"text")],default_langauge="english",name="h1index")
	#for this doc { _id: 1, idioma: "portuguese", quote: "A sorte protege os audazes" }
	# We can create the key as db.quotes.createIndex({ quote : "text" },{ language_override: "idioma" } )
	#To set name:
	#db.stores.create_index([('name', "text"), ('description', "text")],{"default_langauge":"english"},{"name":"h1index"})

def get_all_indices(db):
	for index in db.stores.list_indexes():
		print(index)

def perform_text_query(db):
	#Will print all the rows that have either java, coffee or shop in them. 
	cursor=db.stores.find({'$text': {'$search': "java coffee shop"}}):
	for i in cursor:
		print i

def exact_query(db):
	#find where search term is coffee shop or only java
	cursor=db.stores.find({'$text': {'$search': "Java \"coffee shop\"" }})
	for i in cursor:
		print i	

def term_exlusion(db):
	cursor=db.stores.find({'$text': {'$search': "java shop -coffee"}})
	for i in cursor:
		print i	

def sort_query(db):
	cursor = db.stores.find(
            {'$text': {'$search': 'java coffee shop'}},
            {'score': {'$meta': 'textScore'}})

        # Sort by 'score' field.
    cursor.sort([('score', {'$meta': 'textScore'})]) #<<<< HERE
    for i in cursor:
    	print 

if __name__=="__main__":
	try:
		db=establish_connection()
           #     print 'hello '+str(db)
		insert_data(db)
		#print "1"
		create_text_index(db)
		get_all_indices(db)
		#print db.stores.getIndexes()
		#print "2"
		# print "\n\nThe result of query java coffee shop is:"
		# perform_text_query(db)
		# #print "3"
		# print "\n\nThe result of query either java or \"coffee shop\" is:"
		# exact_query(db)
		# print "\n\nThe result of query either java or shop but not coffee is:"
		# term_exlusion(db)
		# print "\n\n The result in sorted order for query of java cofee shop is:"
		# sort_query(db)
		db.drop_indexes() #drop all the indexes in this collection
		db.stores.drop()

	except Exception, e:
		raise e	
