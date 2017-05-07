from conversation import Conversation
from crud import Crud
from seeder import Seeder

# the main file to be compile in the first time

crud = Crud()

# insert a bulk of data, read the data from the csv file
seeder = Seeder('data/conversation_seeder.csv')
parse_seeder = seeder.csv_file()

for conversation_id, user_id, direction, message in parse_seeder:
    conversation = Conversation(conversation_id, user_id, direction, message)
    crud.create(conversation.content())

# get data based on id
"""
id = "108"
print crud.get(id)
"""

# to get list of data
"""
page = 4
limit = 2
print crud.list(page, limit)
"""

# to update certain i, id = 109

id = 102
tobe_updated_data = {}
updated_data = {'message':'try to update message xxxxxxxxx', 'messagecvcvc':'try to update message xxxxxxxxx', 'conversation_id':'78876'}
tobe_updated_data['user_id'] = '' if 'user_id' not in updated_data else updated_data['user_id']
tobe_updated_data['direction'] = '' if 'direction' not in updated_data else updated_data['direction']
tobe_updated_data['message'] = '' if 'message' not in updated_data else updated_data['message']

conversation = Conversation(id, tobe_updated_data['user_id'], tobe_updated_data['direction'], tobe_updated_data['message'])
result = crud.update(id, conversation.content_update())
print result
# print crud.update(id, updated_data)
# print crud.get(id)

print 'all data ', crud.get_all()


# to delete certain i, id = 109

"""
id = 1090
print crud.remove(id)
print 'all data ', crud.get_all()
"""