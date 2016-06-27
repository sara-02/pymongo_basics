from pymongo import MongoClient

def establish_connection():
	connection=MongoClient("localhost:27017")
	db=connection.abc
	return db

def insert_data(db):
	db.abc.insert({ 'a': 5, 'b': 5, 'c': 'null' })
	db.abc.insert({ 'a': 3, 'b': 'null', 'c': 8 })
	db.abc.insert({ 'a': 'null', 'b': 3, 'c': 9 })
	db.abc.insert({ 'a': 1, 'b': 2, 'c': 3 })
	db.abc.insert({ 'a': 2, 'c': 5 })
	db.abc.insert({ 'a': 3, 'b': 2 })
	db.abc.insert({ 'a': 4 })
	db.abc.insert({ 'b': 2, 'c': 4 })
	db.abc.insert({ 'b': 2 })
	db.abc.insert({ 'c': 6 })

def get_all(db):
	for value in db.abc.find():
		print value

def exists_try(db,value,bool):
	for i in db.abc.find( { value: { '$exists': bool } } ):
			print i

if __name__ == "__main__":
	
	try:
		db = establish_connection()
		insert_data(db)
		print "All"
		get_all(db)
		print "\n\nWhen exists is true"
		exists_try(db,'a',True)
		print "\n\nWhen exists is false"	
		exists_try(db,'b',False)
		
		db.abc.drop()
			
	except Exception, e:
		raise e				