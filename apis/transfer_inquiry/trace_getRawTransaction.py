#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_getRawTransaction.py
@time: 2020/1/6 11:30 上午
@desc:
'''
import logging

from apis.API import request_Api


def getRawTransaction(api_name, params):
	'''
	根据交易hash查询交易字节
	api_name = api_name
	params = 交易hash
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getRawTransaction","params":, "id": 3}' -H "Content-Type:application/json"
	:return: 交易字节信息
	'''
	try:
		rawTransaction = request_Api(api_name, params)
		print(rawTransaction)
		return rawTransaction
	except Exception as e:
		print("根据交易hash查询交易字节,api返回错误".format(e))
		logging.info("根据交易hash查询交易字节,api返回错误".format(e))
		return -1


def getTransaction(api_name, params):
	'''
	根据交易hash查询交易详细信息
	params = 交易hash
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getTransaction","params":["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
	:return: 交易详细信息
	'''
	try:
		transaction = request_Api(api_name, params)
		print(transaction)
		return transaction
	except Exception as e:
		print("根据交易hash查询交易详细信息,api返回错误".format(e))
		logging.info("根据交易hash查询交易详细信息,api返回错误".format(e))
		return -1


def decodeTrasnaction(api_name, params):
	'''
	把交易字节信息反解析成交易详情
	:e.g
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_decodeTrasnaction","params":["0x02a7ae20007923a30bbfbcb998a6534d56b313e68c8e0c594a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002011102011003030000bc9889d00b004120eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params: 交易字节信息 必须为数组
	:return: 交易详情
	'''
	try:
		deTransaction = request_Api(api_name, params)
		print(deTransaction)
		return deTransaction
	except Exception as e:
		print("把交易字节信息反解析成交易详情,api返回错误".format(e))
		logging.info("把交易字节信息反解析成交易详情,api返回错误".format(e))
		return -1


# 目前为未分页效果，分页未实现
# 得到地址中所有交易
def getSendTransactionByAddr(api_name, params):
	'''
	根据地址查询该交易发出的交易，支持分页，从0开始计数，返回结果中的nonce为交易序号
	e.g:
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getSendTransactionByAddr","params":["0x7923a30bbfbcb998a6534d56b313e68c8e0c594a",1,10], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  1. 交易地址 2. 分页号（从1开始）3. 页大小
	:return: 交易列表
	'''
	try:
		seTransaction = request_Api(api_name, params)
		print(seTransaction)
		return seTransaction
	except Exception as e:
		print("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		logging.info("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		return -1


def getReceiveTransactionByAd(api_name, params):
	'''
	根据地址查询该交易接受的交易，支持分页
	e.g:
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getReceiveTransactionByAddr","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5",1,10], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  1. 交易地址; 2. 分页号（从1开始）3. 页大小
	:return: 交易列表
	'''
	try:
		reTransaction = request_Api(api_name, params)
		print(reTransaction)
		return reTransaction
	except Exception as e:
		print("根据地址查询该交易接受的交易，支持分页,api返回错误".format(e))
		logging.info("根据地址查询该交易接受的交易，支持分页,api返回错误".format(e))
		return -1


def rebuild(api_name, params):
	'''
	重建trace中的区块记录
	e.g:
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_rebuild","params":[1,10], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  1. 起始块（包含）2. 终止块（不包含）
	:return:
	'''
	try:
		seTransaction = request_Api(api_name, params)
		print(seTransaction)
		return seTransaction
	except Exception as e:
		print("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		logging.info("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_getSendTransactionByAddr"
	params = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0", 1, 10]
	# params = [1, 10]
	getSendTransactionByAddr(api_name, params)
