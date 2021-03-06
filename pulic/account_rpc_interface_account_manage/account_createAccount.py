#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: v1_account_createAccount.py
@time: 2020/1/8 5:38 下午
@desc:
'''

from pulic.API import request_Api

'''2. account_createAccount'''


def createAccount(api_name, params):
	'''
	创建本地账号
	:param api_name: "account_createAccount"
	:param params:
	:return: 新账号地址信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_createAccount","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("创建本地账号成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("创建本地账号失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_createAccount"
	params = []
	createAccount(api_name, params)