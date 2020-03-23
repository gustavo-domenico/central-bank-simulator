#!env/bin/python
from flask import Flask, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth

import xmltodict
import random

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "doe"
}

protocols = {
	
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False

@app.route('/staws/arquivos', methods=['POST'])
@auth.login_required
def request_protocol():
	if request.content_type != "application/xml":
		abort(400)

	request_data = xmltodict.parse(request.data)
	new_protocol = random.randrange(1000000) 
	protocols[new_protocol] = request_data

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

if __name__ == '__main__':
    app.run(debug=True)