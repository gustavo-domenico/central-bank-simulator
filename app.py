#!env/bin/python
from flask import Flask

from controllers import admin
from controllers import protocols
from controllers import uploads
from controllers import downloads

app = Flask(__name__)

app.register_blueprint(admin.api)
app.register_blueprint(protocols.api)
app.register_blueprint(uploads.api)
app.register_blueprint(downloads.api)

if __name__ == '__main__':
    app.run(debug=True)