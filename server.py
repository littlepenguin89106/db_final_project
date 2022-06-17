from waitress import serve
from paste.translogger import TransLogger
from app import app

serve(TransLogger(app),host='localhost',port=5000)