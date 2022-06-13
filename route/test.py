from flask import Blueprint

from .utils.response import HTTPResponse, HTTPError
from .utils.request import Request

from db.DataBase import DataBase

__all__ = ['test_api']

test_api = Blueprint('test_api', __name__)


@test_api.route('/post', methods=['POST'])
@Request.json('key1: str', 'key2: int')
def test_post(key1, key2):
    try:
        return HTTPResponse(data={'ret1':key1,'ret2':key2},message='test success')
    except:
        return HTTPError('unknown error', 406)



@test_api.route('/get', methods=['GET'])
@Request.args('val1','val2')
def test_get(val1,val2):
    with DataBase() as db:
        test_data = db.get_algo_all()
    try:
        # return HTTPResponse(data={'ret1':val1,'ret2':val2},message='test success')
        return HTTPResponse(data=test_data, message='test success')
    except:
        return HTTPError('unknown error', 406)
        

@test_api.route('/patch', methods=['PATCH'])
@Request.json('key1: list','key2: dict')
def test_patch(key1,key2):
    try:
        return HTTPResponse('test success')
    except:
        return HTTPError('unknown error', 406)
