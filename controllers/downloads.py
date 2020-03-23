from flask import Blueprint, abort, jsonify, request, make_response

import xmltodict
import random
import base64

from common import auth
from common import state

api = Blueprint('downloads', __name__)

@api.route('/staws/arquivos/<path_protocol>/conteudo', methods=['GET'])
@auth.auth.login_required
def request_protocol(path_protocol):
	protocol = int(path_protocol)
	if protocol not in state.protocols:
		abort(404)

	protocol_info = state.protocols[protocol]

	response = make_response(base64.b64decode(state.files[protocol]), 200)
	response.headers["Content-Disposition"] = "attachment; filename=%s" % protocol_info["Parametros"]["NomeArquivo"]

	return response
