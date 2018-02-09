from flask import Blueprint, redirect, url_for

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    """Redirect home page to docs page."""
    return redirect(url_for('api.index'))


@main_bp.route('/docs/<endpoint>', methods=['GET'])
def docs(endpoint):
    """Document page for an endpoint."""
    pass
