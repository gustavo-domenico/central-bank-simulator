from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "john": "doe"
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False