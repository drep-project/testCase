#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_readContract.py
@time: 2020/3/13 1:53 pm
@desc:
'''


from pulic.API import request_Api

'''account_readContract'''

def readContract(api_name, params):
	'''
	读取智能合约（无数据被修改）
	:param api_name: account_readContract
	:param params: 合约地址;合约接口
	:return: 查询结果
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_readContract","params":["0xec61c03f719a5c214f60719c3f36bb362a202125","0xecfb51e10aa4c146bf6c12eee090339c99841efc","0x6d4ce63c"],"id":1}' http://127.0.0.1:15645
	响应：{"jsonrpc":"2.0","id":1,"result":""}
	'''
	try:
		result = request_Api(api_name, params)
		print("读取只能合约内容{}".format(result))
		return result
	except Exception as e:
		print("读取只能合约内容错误{}".format(e))
		return e


if __name__ == '__main__':
	api_name = "account_readContract"
	params = ["0xff4EC27D4C865628602433C0130578bF0e7B7754"]
	readContract(api_name, params)