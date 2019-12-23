#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: api_lock_unlock.py
@time: 2019/12/23 5:20 下午
@desc:
'''
from apis.API import request_Api
import logging


def lock(api_name, lock_account):
	'''
	account_lockAccount
	锁定账号
	:param api_name: account_lockAccount
	:param params:
	:return:
	'''
	
	result = request_Api(api_name, lock_account)
	print(result)
	logging.info("账号{}锁住成功{}".format(api_name, result))


def unlock(api_name, unlock_account):
	'''
	account_account_unlockAccount
	解锁账号
	:param api_name:
	:param params:
	:return:
	'''
	result = request_Api(api_name, unlock_account)
	print(result)
	logging.info("账号{}解锁成功{}".format(api_name, result))


if __name__ == '__main__':
	api_name = "account_lockAccount"
	params = ["0x01bBF4c3d0EcDbbc572E0078dB768F4AEe883e0C"]
	# result = lock(api_name, params)
	result = unlock(api_name, params)
	print(result)
