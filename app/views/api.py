from flask import Blueprint, render_template, jsonify, request

api = Blueprint('api', __name__)

data = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'build the web'},
    'todo3': {'task': 'write document for api'},
}


@api.route('/', methods=['GET'])
def index():
    """List all API to this page."""
    return render_template('api_index.html')


@api.route('/get_todo', methods=['GET'])
def get_todo():
    return jsonify(data)


@api.route('/add_todo', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        todo = request.get_json(silent=True)
        data[todo['name']] = {'task': todo['task']}
        return 'New todo added: {}'.format(todo)


@api.route('/delete_todo', methods=['GET', 'POST'])
def delete_todo():
    name = request.args.get('name') if request.method == 'GET' else request.get_json()['name']

    if name and name in data:
        del data['name']
        return 'Todo has been deleted: {}'.format(name)
    else:
        return 'No matched todo found.'
