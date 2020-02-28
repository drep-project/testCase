#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: unlock_account.py
@time: 2020/2/24 4:02 pm
@desc:
'''
import json
import logging

from transaction_account.API import request_Api

'''5. account_account_unlockAccount'''


def unlockAccount(api_name, params):
	'''
	解锁账号
	:param api_name: account_unlockAccount
	:param params:账号地址
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"], "id": 3}' -H "Content-Type:application/json"
	'''
	result = request_Api(api_name, params)
	try:
		#result =result["result"]
		print("解锁成功{}".format(result))
		return result
	except:
		logging.error("解锁失败，api返回错误，返回值为{}".format(result))
		#print("解锁失败，api返回错误，返回值为{}".format(e))
		return


if __name__ == '__main__':
	api_name = "account_unlockAccount"
	params = ["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"]
	unlockAccount(api_name, params)