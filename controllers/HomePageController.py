from flask import Flask, Blueprint
home_page = Blueprint('home_page', __name__)

@home_page.route('/')
def index():
    return "<h1>Welcome to Swapnil's greatness<h1>"