# !/usr/bin/env python
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


def sendRawTransaction(api_name, params):
	try:
		transfer_result = request_Api(api_name, params)
		result = transfer_result["results"]
		print("交易池返回结果:{}".format(result))
		logging.info("交易池返回结果:{}".format(result))
	except Exception as e:
		print("交易池返回错误:{}".format(e))


if __name__ == '__main__':
	api_name = "blockmgr_sendRawTransaction"
	params = [
		"0x40a287b6d30b05313131317a4120dd8c23c40910d038fa43b2f8932d3681cbe5ee3079b6e9de0bea6e8e6b2a867a561aa26e1cd6b62aa0422a043186b593b784bf80845c3fd5a7fbfe62e61d8564"]
	sendRawTransaction(api_name, params)
