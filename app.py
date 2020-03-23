#!env/bin/python
from flask import Flask

from controllers import admin
from controllers import protocols
from controllers import uploads

app = Flask(__name__)

app.register_blueprint(admin.api)
app.register_blueprint(protocols.api)
app.register_blueprint(uploads.api)

if __name__ == '__main__':
    app.run(debug=True)