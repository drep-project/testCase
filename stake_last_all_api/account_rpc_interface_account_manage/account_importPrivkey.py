#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_importPrivkey.py
@time: 2020/1/8 5:58 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''20. account_importPrivkey'''


def importKeyStore(api_name, params):
	'''
	导入私钥
	:param api_name: "account_importPrivkey"
	:param params:privkey(compress hex)
	:return: address
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_importPrivkey","params":["0xe5510b32854ca52e7d7d41bb3196fd426d551951e2fd5f6b559a62889d87926c"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("导入keystore成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("导入keystore失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_importPrivkey"
	params = ["0xe5510b32854ca52e7d7d41bb3196fd426d551951e2fd5f6b559a62889d87926c"]
	importKeyStore(api_name, params)
