from pymongo import MongoClient
from time import strftime

##Lets make a script to initialize all the collections with my info..

uri='mongodb://localhost:27017/'
db='beatdb'

dbclient = MongoClient(uri)
db = dbclient[db]

users = db['users']
posts = db['posts']
categories = db['categories']
settings = db['settings']

new = {}
new['ident'] = '1d2fb3a4'
new['username'] = 'mattttt'
new['password'] = 'letmein'
new['qty'] = '15'
new['last'] = '234562035'
new['added'] = '123455349'
new['admin'] = True

users.insert(new)

