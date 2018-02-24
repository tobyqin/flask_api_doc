from flask import Blueprint, redirect, url_for, render_template

from .. import get_app

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    """Redirect home page to docs page."""
    return redirect(url_for('api.index'))


@main.route('/docs/<endpoint>', methods=['GET'])
def docs(endpoint):
    """Document page for an endpoint."""
    api = {
        'endpoint': endpoint,
        'methods': [],
        'doc': '',
        'url': '',
        'name': ''
    }

    try:
        func = get_app().view_functions[endpoint]

        api['name'] = _get_api_name(func)
        api['doc'] = _get_api_doc(func)

        for rule in get_app().url_map.iter_rules():
            if rule.endpoint == endpoint:
                api['methods'] = ','.join(rule.methods)
                api['url'] = str(rule)

    except:
        api['doc'] = 'Invalid api endpoint: "{}"!'.format(endpoint)

    return render_template('api_docs.html', api=api)


def _get_api_name(func):
    """e.g. Convert 'do_work' to 'Do Work'"""
    words = func.__name__.split('_')
    words = [w.capitalize() for w in words]
    return ' '.join(words)


def _get_api_doc(func):
    if func.__doc__:
        return func.__doc__
    else:
        return 'No doc found for this API!'
