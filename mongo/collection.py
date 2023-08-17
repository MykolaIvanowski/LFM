# Get the database using the method we defined in pymongo_test_insert file
from .bd import get_database


dbname = get_database()
collection_name = dbname["user_1_items"]

# insert
item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])

# Get the database using the method we defined in pymongo_test_insert file
from .bd import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"] # назва колекції у базі даних 'user_shopping_list'

item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    print(item)

# Get the database using the method we defined in pymongo_test_insert file
from .bd import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

# Create an index on the collection
category_index = collection_name.create_index("category")