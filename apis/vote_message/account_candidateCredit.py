#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_candidateCredit.py
@time: 2020/1/8 3:08 下午
@desc:
'''

from apis.API import request_Api


def candidateCredit(api_name, params):
	'''
	质押成为候选节点 ，候选节点质押
    curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_candidateCredit","params":["0x12d11931447fa47827198c37e838feb52e41e0c9","0x23","0x110","0x30000","{\"Pubkey\":\"0x02e2122ea24230a23dbcaa7f65b268740e29aef65a2deb5bf9c81ec6745d44eafa\",\"Node\":\"192.168.31.51:44444\"}"],"id":1}' http://127.0.0.1:35645
	:param api_name:
	:param params:
	:return: 交易hash
	'''
	try:
		result = request_Api(api_name, params)
		print("质押成为候选节点,返回值为{}".format(result))
	except Exception as e:
		print("质押成为候选节点报错，{}".format(e))


if __name__ == '__main__':
	api_name = "account_candidateCredit"
	params = ["0x0c7c8290eC7E46553656b28F83d68A540C84be60", "0x23", "0x110", "0x30000",
	          "{\"Pubkey\":\"0x0329d20396602ed8a4fdd270aa653d2b9faaa9e650723179d47492d8213a597d91\",\"Node\":\"192.168.31.51:44444\"}"]
	candidateCredit(api_name, params)
