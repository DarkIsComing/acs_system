from flask import render_template, flash, redirect, url_for, request, jsonify
from . import api

#home起始页
@api.route('/',methods=['GET'])
def index():
    return 'hello world'          #直接跳转到首页index