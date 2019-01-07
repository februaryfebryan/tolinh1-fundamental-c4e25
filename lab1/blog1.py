from pymongo import MongoClient


#dbuser => admin, dbpassword = admin1
uri = "mongodb://admin:admin1@ds135852.mlab.com:35852/c4e25"

# step 1: connect to database (mlab)
client =  MongoClient(uri)
# step 2: get a database
db = client.get_database()
# step 3: get a connection
post_collection = db["posts"]
# step 4: create a document
new_post = {
    "title": "Hôm nay trời nhiều mây",  #field title
    "content": "Tôi ra đường, à thôi ở nhà code"  #field content
}
# step 5: insert a document
# post_collection.insert_one(new_post) # underscore
# Toi O nha code
#toi_o_nha_code

# step 6: Close connection
client.close()

# lazy loading
post_list = post_collection.find() #Cursor database
# first_post = post_list[1]
# print(first_post)

for p in post_list:
    print(p)