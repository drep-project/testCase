#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_getPoolTransactions.py
@time: 2020/1/7 6:04 下午
@desc:
'''


from apis.API import request_Api

def getPoolTransactions(api_name, params):
	'''
	获取交易池中的交易信息
	:param api_name:
	:param params: 待查询地址
	:return: 交易池中所有交易
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_getPoolTransactions","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	result = request_Api(api_name, params)
	print(result)
	
if __name__ == '__main__':
	api_name = "blockmgr_getPoolTransactions"
	params = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0"]
	getPoolTransactions(api_name, params)