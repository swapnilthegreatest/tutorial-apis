from flask import Flask
from controllers.HomePageController import home_page
from controllers.UserController import user_controller

if __name__ == '__main__':
        service_app = Flask(__name__)
        service_app.register_blueprint(home_page)
        service_app.register_blueprint(user_controller)
        service_app.run(port=8081)