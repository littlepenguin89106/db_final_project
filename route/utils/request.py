import time
import json
from functools import wraps
from flask import request
from .response import *

__all__ = (
    'Request',
    'timing_request',
    'get_ip',
)

type_map = {
    'int': int,
    'list': list,
    'str': str,
    'dict': dict,
    'bool': bool,
    'None': type(None)
}

def map_dec_params(params):
    str_list_map = map(lambda s: s.split(':', 1), params)
    return map(conv_type, str_list_map)


def conv_type(str_list):
    type_result = (str_list[1:] or None) and type_map.get(str_list[1].strip())
    return (str_list[0]), (type_result)


def repl_underscore(key):
    split_key = filter(bool, key.split('_'))
    join_capitalize = lambda first, *others: (first + ''.join(
        map(str.capitalize, others)))
    return join_capitalize(*split_key)


def check_val_type(val, val_type):
    if (val_type is None) or (type(val) is val_type):
        return val
    else:
        raise ValueError(f"val:{val} is not matched type {val_type}")


class _Request(type):
    def __getattr__(self, content_type):
        def get(*keys, vars_dict={}):
            def data_func(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    data = getattr(request, content_type)
                    if data == None:
                        return HTTPError(
                            f'Unaccepted Content-Type {content_type}', 415)
                    try:
                        for k, t in map_dec_params(keys):
                            repl_k = repl_underscore(k)
                            kwargs.update(
                                {k: check_val_type(data.get(repl_k), t)})
                    except ValueError as ve:
                        return HTTPError('Requested Value With Wrong Type',
                                         400)
                    kwargs.update(
                        {v: data.get(vars_dict[v])
                         for v in vars_dict})
                    return func(*args, **kwargs)

                return wrapper

            return data_func

        return get


class Request(metaclass=_Request):
    pass


def timing_request(func):
    '''
    inject the execution time into response
    the func must return a response with json
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # calculate execution time and get the response
        start = time.time()
        resp, status_code = func(*args, **kwargs)
        exec_time = f'{time.time() - start:.2f}s'
        # load response data
        data = resp.data
        data = json.loads(data)
        # inject execution time into response
        if data['data'] is None:
            data['data'] = {}
        data['data'].update({'__execTime': exec_time})
        resp.data = json.dumps(data)
        return resp, status_code

    return wrapper


def get_ip() -> str:
    ip = request.headers.get('X-Forwarded-For', '').split(',')[-1].strip()
    return ip
