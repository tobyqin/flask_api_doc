from flask import Blueprint, render_template

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def index():
    """List all API to this page."""
    return render_template('api_index.html')
