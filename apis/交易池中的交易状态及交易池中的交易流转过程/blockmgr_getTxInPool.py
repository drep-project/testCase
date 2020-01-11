#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_getTxInPool.py
@time: 2019/12/27 3:16 下午
@desc:
'''
from apis.API import request_Api
import logging


def blockmgrGetTxInPool(api_name, params):
	'''
	获得在交易池中的交易
	:param api_name:
	:param params:
	:return:
	'''
	try:
		pool = request_Api(api_name, params)
		pool_result = pool["results"]
		print("交易池返回结果:{}".format(pool_result))
		logging.info("交易池返回结果:{}".format(pool_result))
	except Exception as e:
		print("交易池返回错误:{}".format(e))


if __name__ == '__main__':
	api_name = "blockmgr_getTxInPool"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5"]
	blockmgrGetTxInPool(api_name, params)
