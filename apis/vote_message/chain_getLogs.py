#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getLogs.py
@time: 2020/1/8 3:58 下午
@desc:
'''

from apis.API import request_Api


def getLogs(api_name, params):
	'''
	根据txhash获取交易log信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getLogs","params":["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"], "id": 3}' -H "Content-Type:application/json"

	:param api_name:
	:param params: txhash 交易哈希
	:return: []log
	'''
	result = request_Api(api_name, params)
	print(result)


if __name__ == '__main__':
	api_name = "chain_getLogs"
	params = ["0x7a2598656bff0a64202f0371ed2646882443a1875ee67c213588db782ff42219"]
	getLogs(api_name, params)
