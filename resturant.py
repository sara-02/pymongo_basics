#Practise codes from the official MongoDB-Pymongo Documentation
#Link:https://docs.mongodb.com/getting-started/python/
#After Downloading the dataset use the followiing command
# mongoimport --db test --collection restaurants --drop --file ~/Downloads/primer-dataset.json

from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from datetime import datetime
import pymongo

def establish_connection():
	client=MongoClient("localhost:27017") #first step connect to the mongoDB
	db=client.test #second step go to the database
	coll=db.restaurants #assign the desired collection
	return coll
	#return db

def insert_data(coll):	
	result=coll.insert_one({
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    })
	print "The resturant id is %s"% str(result.inserted_id)

def print_values(cursor,message):
	print message
	for doc in cursor:
		print doc

def find_all(coll):
	#This is query all the documents in the collection
	
	cursor=coll.find()
	return cursor
	# for doc in cursor:
	# 	print doc

def top_level(coll):
	#Find only in the top level items
	cursor=coll.find({'borough':'Manhattan'}) 		
	return cursor

def embedded_level(coll):
	#Finds only the docs that match this embedded item<i.e key inside a key...>
	cursor=coll.find({'address.zipcode':'10075'})
	return cursor


def greater_than(coll):
	cursor=coll.find({"grade.score":{"$gt":30}})
	return cursor

def lesser_than(coll):
	cursor=coll.find({"grade.score":{"$lt":10}})
	return cursor	

def logical_and(coll):
	# If you give more than one element to find, then it is by default anded.
	cursor=coll.find({"cuisine": "Italian", "address.zipcode": "10075"})
	#The above query is as good as the following one:
	#coll.find({'$and':[{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})
	return cursor

def	logical_or(coll):
	cursor=coll.find({'$or':[{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})
	return cursor

def sorted_results(coll):
	#specify a list of keys to sort by,along with the order of sorting
	cursor=coll.find()
	#can also specify 1,-1 for the direction
	cursor.sort([("borough",pymongo.ASCENDING),("address.zipcode",pymongo.ASCENDING)])
	return cursor

def update_top_level(coll):
	result =coll.update_one(
		{"name": "Juni"},
    	{
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    	}
		)
	return (result.matched_count,result.modified_count)
	

def update_embedded_level(coll):
	result=coll.update_one(
	{"restaurant_id":"41156888"},
	{"$set":{"address.street":"East 31st Street"}})
	return (result.matched_count,result.modified_count)

def update_multiple_docs(coll):
	result=coll.update_many(
		{"address.zipcode": "10016", "cuisine": "Other"},
    	{
        "$set": {"cuisine": "Category To Be Determined"},
        "$currentDate": {"lastModified": True}
    	}
	)
	return (result.matched_count,result.modified_count)

def update_results(matched,modified,message):
	print message
	print "The number of matched entries are %d and the number of modified entries are %d"%(matched,modified)

def doc_replace(coll):
	#One can replace the whole document, after which the new doc will have only the replaced fields and values.
	result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
	)

	return (result.matched_count,result.modified_count)

def create_single_index(coll):
	index_name=coll.create_index([("cuisine",pymongo.ASCENDING)])
	return index_name	

def create_compound_index(coll):
	index_name=coll.create_index([("cuisine",pymongo.ASCENDING),("address.zipcode",pymongo.DESCENDING)])
	return index_name

def group_by_count(coll):
	cursor=coll.aggregate(
		[{"$group":{"_id":"$borough","count":{"$sum":1}}}]
		)
	# The above code will aggreate on the basis of borough, and give the sum of number of entry for each type.
	return cursor

def group_match_count(coll):
	cursor=coll.aggregate(
		[{"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
        ]
		)
	return cursor

def del_one(coll):
	#Deletes the first doc that matches the query
	result=coll.delete_one({"borough":"Staten Island"})
	return result.deleted_count	

def del_many(coll):
	#Deletes all the docs that match the condition
	result=coll.delete_many({"borough":"Manhattan"})
	return result.deleted_count

def rem_all_docs(coll):
	#Remove all the docs from the collection, but not the collection itself
	result=coll.delete_many({})
	return result.deleted_count

def remove_collections(coll):
	#remove the collection, along with all the indexes and meta info if any.
	coll.drop()

def print_del(del_num,message):
	print message
	print "The number of deleted values are %d"%del_num	

def find_info(coll):
	#find function has a scope of single collection only
	returned_cursor=find_all(coll)
	message="\n\nAll Documents in the colletion are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=top_level(coll)
	message="\n\nAll Documents matching the top level query in the colletion are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=embedded_level(coll)
	message="\n\nAll Documents matching the embedded level query in the collection are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=greater_than(coll)
	message="\n\n All Documents with grade greater than 30 are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=lesser_than(coll)
	message="\n\n All Documents with grade lesser than 10 are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=logical_and(coll)
	message="\n\n All Documents with Italian Cuisine AND Zipcode 10075 are:\n"
	print_values(returned_cursor,message)
	
	returned_cursor=logical_or(coll)
	message="\n\n All Documents with Italian Cuisine OR Zipcode 10075 are:\n"
	print_values(returned_cursor,message)
	
	message="\n\n The top level updates are:"
	#print message
	matched,modified=update_top_level(coll)
	update_results(matched,modified,message)

	message="\n\n The embedded level updates are:\n"
	#print message
	matched,modified=update_top_level(coll)
	update_results(matched,modified,message)

	message="\n\nThe number of update many are:\n"
	matched,modified=update_top_level(coll)
	update_results(matched,modified,message)

	message="\n\nAfter replacing the old doc, keeping the _id intact:"
	matched,modified=update_top_level(coll)
	update_results(matched,modified,message)

	message=create_single_index(coll)
	print "The single index name is: %s"%message

	message=create_compound_index(coll)
	print "The compound index name is: %s"%message

	returned_cursor=group_by_count(coll)
	message="\n\n Grouping and counting by Borough type is:\n"
	print_values(returned_cursor,message)

	returned_cursor=group_match_count(coll)
	message="\n\n Grouping and counting by matching specific type of borough and cuisines is:\n"
	print_values(returned_cursor,message)

	del_num=del_one(coll)
	message="\n\n Deleting only one value matching the condition:\n"
	print_del(del_num,message)

	del_num=del_many(coll)
	message="\n\n Deleteing many values matching the condition:\n"
	print_del(del_num,message)

	del_num=rem_all_docs(coll)
	message="\n\n Removing all the exisiting docs in the collection:\n"
	print_del(del_num,message)

	message="\n\n Remove complete collection\n"
	print message
	remove_collections(coll)
	
if __name__=="__main__":
	try:
		coll=establish_connection()
		#insert_data(coll)
		find_info(coll)
		#coll.drop()
	except Exception, e:
		raise e	    