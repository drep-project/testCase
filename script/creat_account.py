#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: creat_account.py
@time: 2020/1/1 11:08 上午
@desc:
'''
import json
from time import sleep
import requests


# 创建账户
def creat_account():
	url = "http://127.0.0.1:15645"
	
	payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_createAccount\",\n\t\"params\":[], \n\t\"id\": 3\n\t\n}"
	headers = {
		'Content-Type': "application/json",
		'cache-control': "no-cache",
		'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
	}
	try:
		response = requests.request("POST", url, data=payload, headers=headers)
		print("creat_account_response:{}".format(response.text))
		jsonDic = json.loads(response.text)
		return jsonDic['result']
	except:
		print("HTTP error")
		response = requests.request("POST", url, data=payload, headers=headers)
		print("creat_account_response:{}".format(response.text))
		return "error Account"

def create_account_100(peoples=100):
	"""
	主业务函数   创建100账户
	:return:
	"""
	account_all = []
	for i in range(peoples):
		# 用户 xxx
		try:
			response = creat_account()
			print("创建用户：", response)
			# sleep(2)
			account_all.append(response)
		except Exception as e:
			print("账户创建失败!".format(e))
			sleep(3)
			print("账户创建失败!".format(e))
			continue
	print("所有账户信息为:{}".format(account_all))
	return account_all


if __name__ == '__main__':
	# log = Logger(filename='../logs/creat_account.log', level='debug')
	api_name = "account_createAccount"
	params = []
	create_account_100(peoples=1000000)
