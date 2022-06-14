from flask import Blueprint

import database

from .utils.response import HTTPResponse, HTTPError
from .utils.request import Request

from database import *

__all__ = ['test_api']

api = Blueprint('api', __name__)

db = database.DataBase()
getter = database.GetManager()
adder = database.AddManager()
updater = database.UpdateManager()
deleter = database.DelManager()


@api.route('/get', methods=['GET'])
# @Request.args('algo_id','algo_name', 'task_name')
def GetAlgo():
    try:
        data = getter.get_algo()
        return HTTPResponse(data, message='GetAlgo success')
    except:
        return HTTPError('unknown error', 406)


@api.route('/post', methods=['POST'])
@Request.json('algo_id: int')
def ShowAlgo(algo_id):
    try:
        data = getter.show_algo(algo_id)
        return HTTPResponse(data, message='ShowAlgo success')
    except:
        return HTTPError('unknown error', 406)


@api.route('/post', methods=['POST'])
@Request.json('paper_id: int')
def ShowPaper(paper_id):
    try:
        data = getter.show_paper(paper_id)
        return HTTPResponse(data, message='ShowPaper success')
    except:
        return HTTPError('unknown error', 406)


@api.route('/post', methods=['POST'])
@Request.json('algo_id: int')
def GetAlgoInfo(algo_id):
    try:
        data = getter.get_algo_info(algo_id)
        return HTTPResponse(data, message='GetAlgoInfo success')
    except:
        return HTTPError('unknown error', 406)


@api.route('/post', methods=['POST'])
@Request.json('algo_id: int', 'description: str')
def UpdateAlgoInfo(algo_id, description):
    try:
        data = updater.update_algo_info(algo_id, description)
        return HTTPResponse(data, message='UpdateAlgo success')
    except:
        return HTTPError('unknown error', 406)


@api.route('/post', methods=['POST'])
@Request.json('algo_id: int', 'description: str')
def DelAlgo(algo_id):
    try:
        data = updater.update_algo_info(algo_id)
        return HTTPResponse(data, message='UpdateAlgo success')
    except:
        return HTTPError('unknown error', 406)