from flask import Blueprint, abort, jsonify, request

import xmltodict
import random

from common import auth
from common import state

api = Blueprint('protocols', __name__)

@api.route('/staws/arquivos', methods=['POST'])
@auth.auth.login_required
def request_protocol():
	if request.content_type != "application/xml":
		abort(400)

	request_data = xmltodict.parse(request.data)
	new_protocol = random.randrange(1000000) 
	state.protocols[new_protocol] = request_data

	response = """
	<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
	<Resultado xmlns:atom="http://www.w3.org/2005/Atom">
 		<Protocolo>%(protocol)s</Protocolo>
 		<atom:link
 			href="https://%(host)s/staws/arquivos/%(protocol)s/conteudo"
 			rel="conteudo" type="application/octet-stream" />
	</Resultado>
	"""

	return response % { 'protocol': new_protocol, 'host': request.host }
