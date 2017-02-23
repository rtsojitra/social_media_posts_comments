from pymongo import MongoClient
import datetime
import hashlib


Users = MongoClient()
db = Users["User_Posts"]

#  create users document
users = db["users"]

# create posts document
posts = db["posts"]


# create user
user = {}
user["username"] = "asojitra"
user["password"] = "myFavPass"
user["email"] = "rt@xcel-it.net"
user["name"] = "Aarti"
users.insert(user)

# add post
inserted_id = user['_id']
name = user["name"]
post = {}
post["text"] = "Hello!!! Morning Friends!"
post["posted"] = datetime.datetime.now()
author = {}
author["id"] = inserted_id
author["name"] = name
post["author"] = author
posts.insert(post)
post_id = post['_id']


# comment 1

comment = {}
comment['user_id'] = "ObjectId('58ae26c7f545d1185c29311e')"
comment['text'] = "GM! How are you??"
comment['posted'] = datetime.datetime.now()
# print post_id
posts.update({'_id': post_id}, {'$set': {'comments': [comment]}})


# comment 2

comment = {}
comment['user_id'] = "ObjectId('58ae2fecf545d1132025a045')"
comment['text'] = "Hey, I am fine, how are you?"
comment['posted'] = datetime.datetime.now()

# print post_id
posts.update({'_id': post_id}, {'$push': {'comments': comment}})

print posts.find({'_id': '58ae2fecf545d1132025a046'})

# below would be how document would look like after executng above queries

#  {
#     "_id" : ObjectId("58ae3483f545d12348b0d12c"),
#     "text" : "Hello!!! Morning Friends!",
#     "author" : {
#         "id" : ObjectId("58ae3483f545d12348b0d12b"),
#         "name" : "Aarti"
#     },
#     "posted" : ISODate("2017-02-22T20:01:55.838Z"),
#     "comments" : [
#         {
#             "text" : "GM! How are you??",
#             "user_id" : "ObjectId('58ae26c7f545d1185c29311e')",
#             "posted" : ISODate("2017-02-22T20:01:55.839Z")
#         },
#         {
#             "text" : "Hey, I am fine, how are you?",
#             "user_id" : "ObjectId('58ae2fecf545d1132025a045')",
#             "posted" : ISODate("2017-02-22T20:01:55.839Z")
#         }
#     ]
# }


