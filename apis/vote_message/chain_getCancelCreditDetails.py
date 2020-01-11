#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getCancelCreditDetails.py
@time: 2020/1/8 3:57 下午
@desc:
'''

from apis.API import request_Api

def getCancelCreditDetails(api_name, params):
	'''
	#获取取消质押详情  可以查log
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetails","params":["0x0ad472fd967eb77fb6e36ec40901790065155d5e"], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:
	:return: 交易详情list，取消的列表 流水
	'''
	result = request_Api(api_name, params)
	print("获取取消质押详情，{}".format(result))
	
	
if __name__ == '__main__':
	api_name = "chain_getCancelCreditDetails"
	params = ["0x0c7c8290eC7E46553656b28F83d68A540C84be60"]
	getCancelCreditDetails(api_name, params)
