import json
import requests


user = 'admin'
password = 'admin'


def login(user, password):
    data = {
        "user": user,
        "password": password
    }
    request_url = "http://127.0.0.1:8005/login"
    res= requests.post(url=request_url, json=data)
    res_text = json.loads(res.content.decode('utf-8'))
    print(res_text)
    return res_text['access_key'], res_text['access_id']

def online(access_key, access_id):
    data = {
        "access_key": access_key,
        "access_id": access_id
    }
    request_url = "http://127.0.0.1:8005/online"
    res= requests.post(url=request_url, json=data)
    res_text = json.loads(res.content.decode('utf-8'))
    if res_text['code'] != 200:
        login(user, password)


def get_task_list(access_key, access_id):
    data = {
        "access_key": access_key,
        "access_id": access_id
    }
    request_url = "http://127.0.0.1:8005/get_task_list"
    res = requests.post(url=request_url, json=data)
    res_text = json.loads(res.content.decode('utf-8', errors='ignore'))
    print(res_text)
    return res_text['data']


def add_task(access_key, access_id, row):
    data = {
        "access_key": access_key,
        "access_id": access_id,
        "data": row
    }
    request_url = "http://127.0.0.1:8005/add_task"
    res= requests.post(url=request_url, json=data)
    res_text = json.loads(res.content.decode('utf-8'))
    print(res_text)
    return res_text['id']


def run_task(access_key, access_id, id):
    data = {
        "access_key": access_key,
        "access_id": access_id,
        "id": id
    }
    request_url = "http://127.0.0.1:8005/run_task"
    res = requests.post(url=request_url, json=data)
    res_text = json.loads(res.content.decode('utf-8'))
    print(res_text)
    if res_text['code'] == 200:
        return True
    else:
        return False


def end_task(access_key, access_id, id):
    data = {
        "access_key": access_key,
        "access_id": access_id,
        "id": id
    }
    request_url = "http://127.0.0.1:8005/end_task"
    res = requests.post(url=request_url, data=data)
    res_text = json.loads(res.content.decode('utf-8'))
    print(res_text)
    if res_text['code'] == 200:
        return True
    else:
        return False