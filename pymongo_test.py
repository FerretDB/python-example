from pymongo import MongoClient
from pymongo.server_api import ServerApi
import argparse

parser = argparse.ArgumentParser(
                    prog='python-example',
                    description='A simple example of using MongoDB with PyMongo',
                    add_help=True)

parser.add_argument('uri') # positional argument
parser.add_argument('-s', '--strict', action='store_true', help='Use strict stable API mode.')

if parser.parse_args().strict:
    server_api = ServerApi('1', strict=True)
    client = MongoClient(parser.parse_args().uri, server_api=server_api)
else:
    client = MongoClient(parser.parse_args().uri)

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
