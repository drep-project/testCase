#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_voteCredit.py
@time: 2020/1/8 11:23 上午
@desc:
'''

from apis.API import request_Api


def voteCredit(api_name, params):
	'''
	投票
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_voteCredit","params":["0x300fc5a14e578be28c64627c0e7e321771c58cd4","0x0ad472fd967eb77fb6e36ec40901790065155d5e","0xf4240","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
	:param api_name:
	:param params:投票参数from地址与to地址 投多少钱 gas价格 手续费
	:return:交易hash
	'''
	try:
		result = request_Api(api_name, params)
		print("投票api返回值为{}".format(result))
	except Exception as e:
		print("投票api返回错误:{}".format(e))


if __name__ == '__main__':
	api_name = "account_voteCredit"
	params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "0xef32f718642426fba949b42e3aff6c56fe08b23c", "0xf4240", "0x110", "0x30000"]
	voteCredit(api_name, params)