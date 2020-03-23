from flask import Blueprint, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth

import xmltodict
import random

import auth

api = Blueprint('protocols', __name__)

protocols_source = {
	
}

@api.route('/staws/arquivos', methods=['POST'])
@auth.auth.login_required
def request_protocol():
	if request.content_type != "application/xml":
		abort(400)

	request_data = xmltodict.parse(request.data)
	new_protocol = random.randrange(1000000) 
	protocols_source[new_protocol] = request_data

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
