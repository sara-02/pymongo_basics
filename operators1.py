from pymongo import MongoClient

def establish_connection():
	connection=MongoClient("localhost:27017")
	db=connection.inventory
	return db

def insert_data(db):
	
	db.inventory.insert({ '_id': 1, 'item': { 'name': "ab", 'code': "123" }, 'qty': 15, 'tags': [ "A", "B", "C" ] })
	db.inventory.insert({ '_id': 2, 'item': { 'name': "cd", 'code': "123" }, 'qty': 20, 'tags': [ "B" ] })
	db.inventory.insert({ '_id': 3, 'item': { 'name': "ij", 'code': "456" }, 'qty': 25, 'tags': [ "A", "B" ] })
	db.inventory.insert({ '_id': 4, 'item': { 'name': "xy", 'code': "456" }, 'qty': 30, 'tags': [ "B", "A" ] })
	db.inventory.insert({ '_id': 5, 'item': { 'name': "mn", 'code': "000" }, 'qty': 20, 'tags': [ [ "A", "B" ], "C" ] })


def get_all(db):
	
	for value in db.inventory.find():
		print value

def eq_operator(db,value):
	
	for p in db.inventory.find({'qty':{'$eq': value}}): 
		#the above operation is equal to db.inventory.find( { qty: value } )
		print p

def eq_embedded(db,value):
	#for embedded key-value keep iterating using the dot notation
	for p in db.inventory.find({"item.name":{'$eq':value}}):
		print p	

def eq_array_ele(db,value):
	for p in db.inventory.find({'tags':{'$eq':value}}):
		print p


# similar to the equals operation other relational operations can also be performed
# $gt-greater than; $gte-greater than or equal to; $lt-less than, ;$lte-less than or equal to; $ne -not equal to

#An addition set of relational operators are $in and $nin-not in. $in is similar to the logical or

def in_values(db,value1,value2,value3=15):
	for p in db.inventory.find({'qty':{ '$in': [ value1, value2, value3 ] } } ):
		print p

def logical_values(db):
	for p in db.inventory.find({'$or': [{'quantity': {'$lt': 15}},{'tags':'B'}]}):
		print p
	# similar operations can be performed on $and, and $not operator. 	  
		
def array_opt(db):
	#The all operator is like the logical and
	print "\n\nArray A,C all--"
	for i in db.inventory.find({'tags': {'$all': [ "A", "C"] } } ):
		print i
	# The size operator matches the array size
	print "\n\n Array Size=1"
	for i in db.inventory.find({'tags': {'$size':1} } ):
		print i

	#element match - Will return the document, if the document in the array has atleast one element matching the criteria
	print "\n\nelement matching"
	for i in db.inventory.find({'tag':{'$elemMatch':{'$eq':'A'}}}):
		print i

	 		

def mod_opt(db):
	#here divisor=3
	#remainder =1
	for i in db.inventory.find({'qty':{'$mod':[3,1]}}):
		print i
if __name__ == "__main__":
	try:
		db = establish_connection()
		insert_data(db)
		# print "ALL_---"
		# get_all(db)
		# value=int(raw_input("Enter the quantity to match:  "))
		# eq_operator(db,value)
		# value=raw_input("Enter the item name to match: ")
		# eq_embedded(db,value)
		# value=raw_input("Enter the tag value to match: ")
		# eq_array_ele(db,value)
		# #One can also find the complete array that can be matched
		# for p in db.inventory.find({'tags': [ "A", "B" ] } ):
		# 	print p

		# svalue=	int (raw_input("Enter the first value to match"))
		# evalue=int (raw_input("Enter the Second value to match"))
		# in_values(db,svalue,evalue)# third is given by default

		# or_values(db)
		# print "\n\nArray A,C all--"
		# array_opt(db)
		mod_opt(db)
		db.inventory.drop()
	except Exception, e:
		raise e			
	