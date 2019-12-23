#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: test.py
@time: 2019/12/23 3:21 下午
@desc:
'''

from apis.api_chain_transaction import *



def chain_getBalance(api_name, params):
	'''

	:return: 查询对应账户的余额
	'''
	logging.info("业务  请求 chain_getBalance")
	try:
		result = request_Api(api_name, params)
		logging.info(result)
	except Exception as e:
		logging.error("查询余额失败,{}".format(e))
		return -1
	return result


def getBalance_of_all_address_list(api_name, address):
	'''
	返回所有余额不为0的账号与账户余额
	:param api_name:
	:param address:
	:return:返回所有余额不为0的账号与账户余额
	'''
	result_list = []  # 余额list
	getBalance_account_list = []  # 余额不为0的账号list
	for i in range(len(address)):
		params = [address[i]]
		try:
			result = request_Api(api_name, params)
		except Exception as e:
			print("查询地址中所有账号余额失败,{}".format(e))
			continue
		logging.info("业务请求: {},result:{}".format(api_name, result))
		result = result["result"]
		if result > 0:
			result_list.append(result)
			getBalance_account_list.append(params)
		else:
			logging.info("结果为:{}".format(result))
	logging.info("有余额的账户为:{},共有{}余额".format(getBalance_account_list, result_list))
	return getBalance_account_list, result_list


# 转账
# 查余额
# 转账100笔
# 查余额
# transaction_one("0x2777fcb6365b64876be85fbfe5e0242ec8852157", "0x712f455a6102987450c2daade60d3f1c8b3b551d")

if __name__ == '__main__':
	rootbalance1 = chain_getBalance(api_name="chain_getBalance",params=["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"])
	balance1 = chain_getBalance(api_name="chain_getBalance",params=["0x016fA969d48C0BeB39e099d88356500Be5b854f3"])
	print("rootbalance1,{},balance1{}".format(rootbalance1,balance1))
	send_account = "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"
	receive_account = "0x016fA969d48C0BeB39e099d88356500Be5b854f3"
	price = "0x2710"
	result = transaction_one(send_account, receive_account, price)
	print("执行一笔交易", result)
	rootbalance2 = chain_getBalance(api_name="chain_getBalance",params=["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"])
	balance2 = chain_getBalance(api_name="chain_getBalance",params=["0x016fA969d48C0BeB39e099d88356500Be5b854f3"])
	print("rootbalance2,{},balance2{}".format(rootbalance2,balance2))
