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

	return response % { 'protocol': new_protocol, 'host': request.host }, 201

@api.route('/staws/arquivos/disponiveis', methods=['GET'])
@auth.auth.login_required
def get_available():
	files = ""

	for key in state.responses:
		value = state.responses[key]

		files += """
	<Arquivo>
		<Protocolo>%s</Protocolo>
		<TipoArquivo>%s</TipoArquivo>
		<CodigoDocumento>1234</CodigoDocumento>
		<Sistema>CAM</Sistema>
		<SituacaoAtual>
			<Codigo>3</Codigo>
			<Descricao>A receber</Descricao>
		</SituacaoAtual>
		<DataHoraDisponibilizacao>2012-07-21T10:00:00.000</DataHoraDisponibilizaca>
	</Arquivo>
		""" % (value["protocol"], value["type"])

	return """ 
			<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
			<Resultado xmlns:atom="http://www.w3.org/2005/Atom">
				<DataHoraProximaConsulta>2012-07-25T10:00:00.001</DataHoraProximaConsulta>
				%s
			</Resultado>
			""" % files
