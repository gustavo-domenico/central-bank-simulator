#!env/bin/python
from flask import Flask

from controllers import admin
from controllers import protocols

app = Flask(__name__)

app.register_blueprint(admin.api)
app.register_blueprint(protocols.api)

if __name__ == '__main__':
    app.run(debug=True)