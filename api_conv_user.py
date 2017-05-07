from flask import Flask, jsonify, abort, request
from flask_restful import Api
import json

from crud.repo import Repo
from crud.conversation import Conversation
from crud.user import User

app = Flask(__name__)
api = Api(app)

repository = Repo()

# REST interface to be implemented
@app.route('/conversations', methods=['POST'])
def create_conversation():
    data = json.loads(request.data)
    if not data:
        abort(404)

    # init conversation
    conversation = Conversation(data['id'], data['user_id'], data['direction'], data['message'])
    result = repository.create(conversation.content())

    return jsonify({'conversation':result}), 201

@app.route('/conversations/<string:id>', methods=['GET'])
def get_conversation(id):
    get_datum = repository.get(id)
    if not get_datum:
        abort(404)
    return jsonify({'conversation':get_datum}), 200

@app.route('/conversations/', methods=['GET'])
def get_all_conversations():
    page = request.args.get('page')
    limit = request.args.get('limit')

    if not page.isdigit() and not limit.isdigit():
        abort(404)

    result = repository.list(int(page), int(limit))
    return jsonify({'conversation': result}), 200

@app.route('/conversations/<string:id>', methods=['PUT'])
def update_conversation(id):
    load_data = json.loads(request.data)

    updated_data = {}
    updated_data['user_id'] = '' if 'user_id' not in load_data else load_data['user_id']
    updated_data['direction'] = '' if 'direction' not in load_data else load_data['direction']
    updated_data['message'] = '' if 'message' not in load_data else load_data['message']

    conversation = Conversation(id, updated_data['user_id'], updated_data['direction'], updated_data['message'])
    result = repository.update(id, conversation.content_update())
    return jsonify({'conversation':result}), 201

@app.route('/conversations/<string:id>', methods=['DELETE'])
def delete_conversation(id):
    result = repository.remove(id)
    return jsonify({'conversation':result}), 200

# user
@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    get_datum = repository.get(id)
    if not get_datum:
        abort(404)
    return jsonify({'user':get_datum}), 200

@app.route('/users/', methods=['GET'])
def get_all_user():
    page = request.args.get('page')
    limit = request.args.get('limit')

    if not page.isdigit() and not limit.isdigit():
        abort(404)

    result = repository.list(int(page), int(limit))
    return jsonify({'user': result}), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = json.loads(request.data)

    if not data:
        abort(404)

    # init user
    user = User(data['id'], data['name'], data['gender'], data['city'], data['phone'], data['email'])
    result = repository.create(user.info())
    return jsonify({'user':result}), 201

@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    load_data = json.loads(request.data)

    updated_data = {}
    updated_data['name'] = '' if 'name' not in load_data else load_data['name']
    updated_data['gender'] = '' if 'gender' not in load_data else load_data['gender']
    updated_data['city'] = '' if 'city' not in load_data else load_data['city']
    updated_data['phone'] = '' if 'phone' not in load_data else load_data['phone']
    updated_data['email'] = '' if 'email' not in load_data else load_data['email']

    user = User(id, updated_data['name'], updated_data['gender'], updated_data['city'], updated_data['phone'], updated_data['email'])
    result = repository.update(id, user.info_update())
    return jsonify({'user':result}), 201

@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    result = repository.remove(id)
    return jsonify({'user':result}), 200

@app.route('/')
def main():
    return 'Task 1'