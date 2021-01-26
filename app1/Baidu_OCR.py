from flask import Blueprint, render_template, redirect,request,flash
import requests as RE
import base64
import os,sys
from app1 import db
from .models import Baidu_OCR

baidu_ocr = Blueprint('Baidu_OCR',__name__)

def get_res(file_path):
	request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
	# 二进制方式打开图片文件
	f = open(file_path, 'rb')
	img = base64.b64encode(f.read())

	params = {"image": img}
	access_token = '24.32373d2292d7c2c7eaec080278e270f6.2592000.1603369340.282335-22679084'
	request_url = request_url + "?access_token=" + access_token
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = RE.post(request_url, data=params, headers=headers)
	response=response.json()
	response=response["words_result"]
	return response
@baidu_ocr.route("/")
def baidu_ocr_index ():
	return render_template('Baidu_OCR/index.html')

@baidu_ocr.route('/get',methods=['POST'])
def ocr():
	file = request.files['file']
	file_path="\\home\\rentu\\"+file.filename
	file.save(file_path)
	result=get_res(file_path)
	return render_template('Baidu_OCR/index.html',res=result)
