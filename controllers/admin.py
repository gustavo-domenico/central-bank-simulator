from flask import Blueprint, request

from common import state

api = Blueprint('admin', __name__)

@api.route('/admin/protocols', methods=['GET'])
def list_protocols():
	return state.protocols

@api.route('/admin/files', methods=['GET'])
def list_files():
	return state.files

@api.route('/admin/response', methods=['POST'])
def add_response():
	state.responses[request.json["protocol"]] = request.json
	print state.responses
	return request.json

