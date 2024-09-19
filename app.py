from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def create_token():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return jwt.encode({'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')

@app.route('/')
def health_check():
    return "Application is running!"

@app.route('/data')
def get_data():
    return jsonify({"data": "This is some mock data!"})

@app.route('/secure', methods=['GET'])
def secure_data():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return jsonify({"data": "This is secured data!"})
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
