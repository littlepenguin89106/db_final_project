from operator import truediv
from flask import Flask
from database.GetManager import GetManager
# from route import api
from route import test_api,be_api

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    api2prefix = [
        (test_api,'/test'),
        (be_api,'/')
    ]
    for api, prefix in api2prefix:
        app.register_blueprint(api, url_prefix=prefix)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='localhost',port=5000,debug=True)
