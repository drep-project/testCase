#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_transfer.py
@time: 2020/1/8 5:41 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''8. account_transfer'''


def transfer(api_name, params):
	'''
	转账
	:param api_name: account_transfer
	:param params:发起转账的地址；接受者的地址；金额；gas价格；gas上限；备注
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_transfer","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000",""],"id":1}' http://127.0.0.1:15645
	'''
	
	try:
		result = request_Api(api_name, params)
		print("转账成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("转账失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_transfer"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000",""]
	transfer(api_name, params)
