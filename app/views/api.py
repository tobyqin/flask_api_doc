import re

from flask import Blueprint, render_template, jsonify, request, url_for

from .. import get_app

api = Blueprint('api', __name__)

data = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'build the web'},
    'todo3': {'task': 'write document for api'},
}


def get_api_map():
    for rule in get_app().url_map.iter_rules():
        if re.search(r'/api/.+', str(rule)):
            yield str(rule), rule.endpoint


@api.route('/', methods=['GET'])
def index():
    """List all API to this page."""
    api_map = sorted(list(get_api_map()))
    index_url = url_for('main.index', _external=True)
    api_map = [(index_url + x[0][1:], x[1]) for x in api_map]
    return render_template('api_index.html', api_map=api_map)


@api.route('/get_todo', methods=['GET'])
def get_todo():
    """Get all todo tasks."""
    return jsonify(data)


@api.route('/add_todo', methods=['POST'])
def add_todo():
    """
    Add a todo task,  please post data in json format, e.g.

    data = {
              "name":"the title",
              "task":"the detail"
            }
    """
    if request.method == 'POST':
        todo = request.get_json(silent=True)
        data[todo['name']] = {'task': todo['task']}
        return 'New todo added: {}'.format(todo)


@api.route('/delete_todo', methods=['GET', 'POST'])
def delete_todo():
    """Delete a todo task."""
    name = request.args.get('name') if request.method == 'GET' else request.get_json()['name']

    if name and name in data:
        del data['name']
        return 'Todo has been deleted: {}'.format(name)
    else:
        return 'No matched todo found.'
