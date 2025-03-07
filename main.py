from flask import Flask, request, jsonify

from controllers.ApiKeyController import security
from controllers.HomePageController import home_page
from controllers.UserController import user_controller
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
# Setup the Flask-JWT-Extended extension

if __name__ == '__main__':
    service_app = Flask(__name__)
    service_app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    service_app.register_blueprint(home_page)
    service_app.register_blueprint(user_controller)
    service_app.register_blueprint(security)
    jwt = JWTManager(service_app)
    service_app.run(port=8081)