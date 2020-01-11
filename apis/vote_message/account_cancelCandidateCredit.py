#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_cancelCandidateCredit.py
@time: 2020/1/8 3:46 下午
@desc:
'''

from apis.API import request_Api


def cancelCandidateCredit(api_name, params):
	'''
	 #取消质押  可以查log
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_cancelCandidateCredit","params":["0x0ad472fd967eb77fb6e36ec40901790065155d5e","0x2386f26fc10000","0x110","0x30000",""],"id":1}' http://127.0.0.1:15645
	:param api_name:
	:param params:
	:return:交易哈希
	'''
	result = request_Api(api_name, params)
	print(result)


if __name__ == '__main__':
	api_name = "account_cancelCandidateCredit"
	params = ["0x0c7c8290eC7E46553656b28F83d68A540C84be60", "0x2386f26fc10000", "0x110", "0x30000", ""]
	cancelCandidateCredit(api_name, params)
