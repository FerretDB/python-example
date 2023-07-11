# Get the database using the method we defined in pymongo_test_insert file 
from pymongo_test_insert import get_database
# dbname = get_database()

def query():
	dbname = get_database()
	# Create a new collection
	collection_name = dbname["user_1_items"]

	item_details = collection_name.find()
	# for item in item_details:
	# 	# This will give readable output, but KeyError
	# 	print(item['item_name'], item['category'])

	###---------------------------------------------------###
	### Comment the above 'for loop' & 'print statements' ### 
	###       for the next lines of code to work          ###
	###---------------------------------------------------###
	from pandas import DataFrame

	# Convert the dictionary objects to dataframe
	items_df = DataFrame(item_details)

	# View all items
	print(items_df)	

	###--------------------------------------------------------###
	### Get items of particular category without and with index###
	###--------------------------------------------------------###
	item_details = collection_name.find({"category" : "food"})
	for item in item_details:
		print(item)
		
	# Add more data to understand the need for indexing
	import pymongo_test_insert_more_items
		
	# Create index on category, as an example
	category_index = collection_name.create_index("category")

	# Execute the previous query again to see the documents scanned (refer to the article)
	for item in item_details:
		# This will give readable output, but KeyError
		print(item['item_name'], item['category'])
