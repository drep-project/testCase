#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: demo_test.py
@time: 2019/12/23 3:21 下午
@desc:
'''
import xlwt

from apis.api_chain_transaction import *
from apis.Utils import *
from xlrd import open_workbook
from xlutils.copy import copy


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

def transfer_balance(api_name, send_account, receive_account, price):
	'''
		执行一笔交易前查询余额,执行一笔交易之后,再次查询余额进行对比

	:param api_name:
	:param send_account:
	:param receive_account:
	:param price:
	:return:
	'''
	
	send_account_balance_before = chain_getBalance(api_name, [send_account])["result"]  # 查询发送交易之前发送账号的余额,并得到result中的值
	receive_account_balance_before = chain_getBalance(api_name, [receive_account])["result"]  # 查询发送交易之前接收交易的账号的余额
	print("send_account发送前余额,{},received_account接收账号之前余额{}".format(send_account_balance_before,
	                                                               receive_account_balance_before))
	result = transaction_one(send_account, receive_account, price)  # 发送一笔交易
	print("执行一笔交易", result)
	result = {
		"send_account": send_account,
		"receive_account": receive_account,
		"price": price,
		"send_account_balance_before": send_account_balance_before,
		"receive_account_balance_before": receive_account_balance_before
	}
	# 写入 Excel  Utils
	excel_write('./before_price.xls', [['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before', 'receive_account_balance_before'],
	                                   [result.get("send_account"), result.get("receive_account"), result.get("price"),
	                                    result.get("send_account_balance_before"),
	                                    result.get("receive_account_balance_before")],
	                                   [result.get("send_account"), result.get("receive_account"), result.get("price"),
	                                    result.get("send_account_balance_before"),
	                                    result.get("receive_account_balance_before")]
	                                   ])
	
	return result


def check_transfer_balance(api_name):
	# 读Excel 文件
	results = excel_read_dict('before_price.xls')
	print(results)
	api_name = "chain_getBalance"
	result_list = []
	for result in results:
		send_account_balance_after = chain_getBalance(api_name, [result["send_account"]])["result"]  # 查询发送交易之前发送账号的余额
		receive_account_balance_after = chain_getBalance(api_name, [result["receive_account"]])[
			"result"]  # 查询发送交易之前接收交易的账号的余额
		
		print("send_account发送账号发送后余额,{},received_account接收账号之后余额{}".format(send_account_balance_after,
		                                                                   receive_account_balance_after))
		result["send_account_balance_after"] = send_account_balance_after
		result["receive_account_balance_after"] = receive_account_balance_after
	# results = results.append(result["send_account_balance_after"])
	# result_list.append(result)
	# print("困困困", result.get("交易金额"))
	
	excel_write('./after_price.xls', [['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before', 'receive_account_balance_before',
	                                   'send_account_balance_after', 'receive_account_balance_after'],
	                                  [result.get("send_account"), result.get("receive_account"),
	                                   result.get("transfer_price"), result.get("send_account_balance_before"),
	                                   result.get("receive_account_balance_before"),
	                                   result.get("send_account_balance_after"),
	                                   result.get("receive_account_balance_after")],
	                                  [result.get("send_account"), result.get("receive_account"),
	                                   result.get("transfer_price"),
	                                   result.get("send_account_balance_before"),
	                                   result.get("receive_account_balance_before"),
	                                   result.get("send_account_balance_after"),
	                                   result.get("receive_account_balance_after")]
	                                  ])


# if results["send_account_balance_before"] > results["send_account_balance_after"]:
# 	results["success"] = "交易成功"
# 	print("发送交易成功!send_account发送账号发送之前余额为,{},send_account发送账号之后余额为{}".format(results["send_account_balance_before"],
# 	                                                                         results["send_account_balance_after"]))
# else:
# 	results["success"] = "交易失败"
# 	print("发送交易失败!send_account发送账号发送之前余额为,{},send_account发送账号之后余额为{}".format(results["send_account_balance_before"],
# 	                                                                         results["send_account_balance_after"]))


# 更新 Excel


#
# return -1

if __name__ == '__main__':
	api_name = "chain_getBalance"
	account = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "0x016fA969d48C0BeB39e099d88356500Be5b854f3"]
	price = "0xf4240"
	transfer_balance(api_name, account[0], account[1], price)
	check_transfer_balance(api_name)
