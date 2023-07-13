from pymongo import MongoClient
import sys

CONNECTION_STRING = str(sys.argv[-1])

client = MongoClient(CONNECTION_STRING)

db = client.test
res = db.command('ping', '1')

print(res)
