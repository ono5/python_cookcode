import datetime

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

# Create DB
db = client['test_database']

# Prepare data
stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

# Insert data to db
db_stacks = db.stacks
# Get "Object ID"
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
print("################")
print(db_stacks.find_one({'_id': stack_id}))

print("################")
print(db_stacks.find_one({'name': 'customer1'}))

print("################")
print(db_stacks.find_one({'pip': ['python', 'java', 'go']}))

print("################")
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))

for stack in db_stacks.find():
    print(stack)

print("################")
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$gt': now}}):
    print(stack)

# Update
db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYY'}})

print(db_stacks.find_one({'name': 'YYY'}))

# Delete
db_stacks.delete_one({'name': 'YYY'})
print(db_stacks.find_one({'name': 'YYY'}))