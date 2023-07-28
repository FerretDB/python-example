from pymongo import MongoClient
from pymongo.server_api import ServerApi
import sys

# if set in the YAML file
if str(sys.argv[-1]) == "StableAPI":
    uri = sys.argv[-2]
    MongoClient(uri, server_api=ServerApi("1", strict=False, deprecation_errors=True))
else:
    uri = sys.argv[-1]

client = MongoClient(uri)

db = client.test
res = db.command('ping', '1')
print(res)

res = db.command('dropDatabase', 'test')
print(res)

for i in range(1, 5):
    db['foo'].insert_one({'_id': i, 'a': i})

res = db['foo'].find_one({'a': 4})
assert (res == {'_id': 4, 'a': 4}), "Value should be 4"
