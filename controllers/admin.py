from flask import Blueprint

from common import state

api = Blueprint('admin', __name__)

@api.route('/admin/protocols', methods=['GET'])
def list_protocols():
	return state.protocols
