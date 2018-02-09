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


@api.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        name = request.args.get('name')
        task = request.args.get('task')
        if not name and not task:
            return 'Should provide name and task in query string!', 400

        data[name] = {'task': task}

    return 'task added: {}'.format(task)
