from flask import Blueprint, abort, jsonify, request

import xmltodict
import random
import hashlib
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

	protocol_info = state.protocols[protocol]

	if int(protocol_info["Parametros"]["Tamanho"]) != int(request.content_length):
		abort(400, "Invalid size provided.")

	content_hash = hashlib.sha256(request.data).hexdigest()
	if protocol_info["Parametros"]["Hash"] != content_hash:
		abort(400, "Invalid hash provided.")

	state.files[protocol] = base64.b64encode(request.data)

	return "", 200
