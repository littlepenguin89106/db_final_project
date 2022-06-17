from flask import Blueprint

from .utils.response import HTTPResponse, HTTPError
from .utils.request import Request

from database import *

__all__ = ['be_api']

be_api = Blueprint('be_api', __name__)

# Search paper
@be_api.route('/get_paper', methods=['GET'])
def GetPaper():
    try:
        data = GetManager().get_paper()
        return HTTPResponse(data=data, message='GetPaper success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)


# Display paper page
@be_api.route('/show_paper', methods=['POST'])
@Request.json('paper_id: int')
def ShowPaper(paper_id):
    try:
        data = GetManager().show_paper(paper_id)
        return HTTPResponse(data=data, message='ShowPaper success')
    except:
        return HTTPError('unknown error', 406)


# Display algorithm page
@be_api.route('/show_algo', methods=['POST'])
@Request.json('algo_id: int')
def ShowAlgo(algo_id):
    try:
        data = GetManager().show_algo(algo_id)
        return HTTPResponse(data=data, message='ShowAlgo success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)

import traceback

# Update algorithm page
@be_api.route('/get_algo', methods=['GET'])
def GetAlgo():
    try:
        data = GetManager().get_algo()
        return HTTPResponse(data=data, message='GetAlgo success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)


@be_api.route('/get_algo_info', methods=['POST'])
@Request.json('algo_id: int')
def GetAlgoInfo(algo_id):
    try:
        data = GetManager().get_algo_info(algo_id)
        return HTTPResponse(data=data, message='GetAlgoInfo success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/update_algo_info', methods=['POST'])
@Request.json('algo_id: int', 'name: str', 'description: str')
def UpdateAlgoInfo(algo_id, name, description):
    try:
        UpdateManager().update_algo_info(algo_id, name, description)
        return HTTPResponse(message='UpdateAlgo success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/exist_algo', methods=['POST'])
@Request.json('algo_id: int')
def ExistAlgo(algo_id):
    try:
        data = GetManager().exist_algo(algo_id)
        return HTTPResponse(data=data, message='ExistAlgo success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)


@be_api.route('/delete_algo', methods=['POST'])
@Request.json('algo_id: int')
def DeleteAlgo(algo_id):
    try:
        DelManager().del_algo(algo_id)
        return HTTPResponse(message='DeleteAlgo success')
    except:
        return HTTPError('unknown error', 406)


# Update paper page
@be_api.route('/update_paper_info', methods=['POST'])
@Request.json('paper_id: int', 'name: str', 'description: str', 'author: str', 'publication: str', 'publish_date: str', 'algo: list', 'task: list')
def UpdatePaperInfo(paper_id, name, description, author, publication, publish_date, algo, task):
    try:
        UpdateManager().update_paper_info(paper_id, name, description, author, publication, publish_date, algo, task)
        return HTTPResponse(message='UpdatePaper success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/delete_paper', methods=['POST'])
@Request.json('paper_id: int')
def DeletePaper(paper_id):
    try:
        DelManager().del_paper(paper_id)
        return HTTPResponse(message='DelPaper success')
    except:
        return HTTPError('unknown error', 406)


# Update bulletin page
@be_api.route('/get_bulletin', methods=['GET'])
def GetBulletin():
    try:
        data = GetManager().get_bulletin()
        return HTTPResponse(data=data, message='GetBulletin success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/update_bulletin_info', methods=['POST'])
@Request.json('bulletin_id: int', 'author: str', 'description: str')
def UpdateBulletinInfo(bulletin_id, author, description):
    try:
        UpdateManager().update_bulletin_info(bulletin_id, author, description)
        return HTTPResponse(message='UpdateBulletinInfo success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/delete_bulletin', methods=['POST'])
@Request.json('bulletin_id: int')
def DeleteBulletin(bulletin_id):
    try:
        DelManager().del_bulletin(bulletin_id)
        return HTTPResponse(message='DeleteBulletin success')
    except:
        return HTTPError('unknown error', 406)


# Upload algorithm page
@be_api.route('/add_algo', methods=['POST'])
@Request.json('algo_name: str', 'description: str')
def AddAlgo(algo_name, description):
    try:
        AddManager().add_algo(algo_name, description)
        print(traceback.format_exc())
        return HTTPResponse(message='AddAlgo success')
    except:
        return HTTPError('unknown error', 406)


# Upload paper page
@be_api.route('/get_task', methods=['GET'])
def GetTask():
    try:
        data = GetManager().get_task()
        return HTTPResponse(data=data, message='GetTask success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/add_paper', methods=['POST'])
@Request.json('name: str', 'description: str', 'author: str', 'publication: str', 'publish_date: str', 'algo: list', 'task: list')
def AddPaper(name, description, author, publication, publish_date, algo, task):
    try:
        AddManager().add_paper(name, description, author, publication, publish_date, algo, task)
        return HTTPResponse(message='AddPaper success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)


# Upload announcement page
@be_api.route('/add_announcement', methods=['POST'])
@Request.json('author: str', 'description: str')
def AddAnnouncement(author, description):
    try:
        AddManager().add_bulletin(author, description)
        return HTTPResponse(message='AddAnnouncement success')
    except:
        return HTTPError('unknown error', 406)


# Get dataset via task_id
@be_api.route('/get_dataset', methods=['POST'])
@Request.json('task_id: int')
def GetDataset(task_id):
    try:
        data = GetManager().get_dataset(task_id)
        return HTTPResponse(data=data, message='GetDataset success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/get_all_dataset', methods=['GET'])
def GetAllDataset():
    try:
        data = GetManager().get_all_dataset()
        return HTTPResponse(data=data, message='GetAllDataset success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/update_dataset', methods=['POST'])
@Request.json('dataset_id: int', 'description: str', 'name: str', 'attribute: str')
def UpdateDataset(dataset_id, description, name, attribute):
    try:
        data = UpdateManager().update_dataset(dataset_id, description, name, attribute)
        return HTTPResponse(data=data, message='UpdateDataset success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/get_task_info', methods=['POST'])
@Request.json('task_id: int')
def GetTaskInfo(task_id):
    try:
        data = GetManager().get_task_info(task_id)
        return HTTPResponse(data=data, message='GetTaskInfo success')
    except:
        print(traceback.format_exc())
        return HTTPError('unknown error', 406)


@be_api.route('/get_dataset_info', methods=['POST'])
@Request.json('dataset_id: int')
def GetDatasetInfo(dataset_id):
    try:
        data = GetManager().get_dataset_info(dataset_id)
        return HTTPResponse(data=data, message='GetDatasetInfo success')
    except:
        return HTTPError('unknown error', 406)

    
@be_api.route('/add_dataset', methods=['POST'])
@Request.json('name: str', 'description: str', 'attribute: str')
def AddDataset(name, description, attribute):
    try:
        data = AddManager().add_dataset(name, description, attribute)
        return HTTPResponse(data=data, message='AddDataset success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/delete_dataset', methods=['POST'])
@Request.json('dataset_id: int')
def DeleteDataset(dataset_id):
    try:
        data = DelManager().del_dataset(dataset_id)
        return HTTPResponse(data=data, message='DeleteDataset success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/get_bulletin_info', methods=['POST'])
@Request.json('bulletin_id: int')
def GetBulletinInfo(bulletin_id):
    try:
        data = GetManager().get_bulletin_info(bulletin_id)
        return HTTPResponse(data=data, message='GetBulletinInfo success')
    except:
        return HTTPError('unknown error', 406)


@be_api.route('/exist_dataset', methods=['POST'])
@Request.json('dataset_id: int')
def ExistDataset(dataset_id):
    try:
        data = GetManager().exist_dataset(dataset_id)
        return HTTPResponse(data=data, message='ExistDataset success')
    except:
        return HTTPError('unknown error', 406)