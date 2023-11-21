from pymongo import MongoClient
import sys

uri = sys.argv[-1]

client = MongoClient(uri)

db = client.test
res = db.command('ping', '1')
assert (res['ok'] == 1.0), "ping failed"

res = db.command('dropDatabase', 1)
assert (res['ok'] == 1.0), "dropDatabase failed"

doc_list = [
    {'_id': 1, 'a': 1},
    {'_id': 2, 'a': 2},
    {'_id': 3, 'a': 3},
    {'_id': 4, 'a': 4},
]

db['foo'].insert_many(doc_list)

actual = db['foo'].find_one({'a': 4})
assert (actual == {'_id': 4, 'a': 4}), "Value should be 4"
