#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getCreditDetails.py
@time: 2020/1/8 11:37 上午
@desc:
'''

from apis.API import request_Api


def getCreditDetails(api_name, params):
	'''
	获得投票信息，查询投票信息
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCreditDetails","params":["0x0ad472fd967eb77fb6e36ec40901790065155d5e"], "id": 3}' -H "Content-Type:application/json"
	:param api_name: chain_getVoteCreditDetails
	:param params: 参数为to的地址,查询的投票的地址
	:return: 1.投票信息 2.质押信息
	'''
	result = request_Api(api_name, params)
	print("投票信息返回为{}".format(result))


if __name__ == '__main__':
	api_name = "chain_getCreditDetails"
	params = ["0x0c7c8290eC7E46553656b28F83d68A540C84be60"]
	getCreditDetails(api_name, params)
