from . import main

@main.route('/')
def index():
    return '<h1>Testing...</h1>'