#!/usr/bin/python
# -*- coding: UTF-8 -*-
from apis.API import request_Api


def creat_one_wallet_account(name, params):
	'''
	
	:param name: api名字
	:param params: api参数
	:return: 创建的一个钱包地址
	'''
	try:
		address = request_Api(name, params)
		print(address)
		address = address['result']
		print("result:{}".format(address))
		return address
	except Exception as e:
		print(e)
	return None


if __name__ == '__main__':
	name = "account_createWallet"
	params = ["1234567"]
	creat_one_wallet_account(name, params)
