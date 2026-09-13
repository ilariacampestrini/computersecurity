from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configure your application to use the flask_jwt_extended package
app.config['JWT_SECRET_KEY'] = 'sup3r-s3cr3t-c0d3!'  # Change this to a strong secret key
app.secret_key = "sup3r-s3cret-k3y!"
jwt = JWTManager(app)

# User datastore (in a real application, use a database)
users = {
    'user1': 'ciaociaociaociaociaociaociao',
    'user2': 'ciao',
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Create an access token
    access_token = create_access_token(identity=username)
    print(access_token)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
