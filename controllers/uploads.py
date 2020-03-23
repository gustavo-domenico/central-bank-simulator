from flask import Blueprint, abort, jsonify, request

import xmltodict
import random
import base64

from common import auth
from common import state

api = Blueprint('uploads', __name__)

@api.route('/staws/arquivos/<path_protocol>/conteudo', methods=['PUT'])
@auth.auth.login_required
def request_protocol(path_protocol):
	protocol = int(path_protocol)
	if protocol not in state.protocols:
		abort(404)

	state.files[protocol] = base64.b64encode(request.data)

	return "", 200
