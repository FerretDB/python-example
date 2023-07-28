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
