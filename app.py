from operator import truediv
from flask import Flask
from route import api

app = Flask(__name__)
app.config['DEBUG'] = True

api2prefix = [
    (api,'/test')
]
for api, prefix in api2prefix:
    app.register_blueprint(api, url_prefix=prefix)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)