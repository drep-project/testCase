#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import logging
import apis.log
import numpy as np
from apis.creat_account import api_create_account as ca
from apis.API import request_Api


# 执行多次 transfer 函数
def transaction_one(send_account, receive_account, price):
	'''
	
	:param rootAccount: 发送账户
	:param receive_account: 接收账户
	:return: 1个账户的交易结果
	'''
	
	api_name = "account_transfer"
	try:
		api_params = [send_account, receive_account, price, "0x110", "0x30000", ""]
		result = request_Api(api_name, api_params)
		result = result['result']
	except Exception as e:
		print("发送一笔交易失败{}".format(e))
		logging.info("发送一笔交易失败{}".format(e))
		return -1
	return result


# 执行多次 transfer 函数
def random_transaction(api_name, send_account, receive_account):
	'''
	
	:param api_name:
	:param receive_account:
	:return:
	'''
	logging.info(receive_account)
	price = ["0x168000000000000", "0x18800000000", "0x16600000000", '0x1580000000', "0x368000000000", "0x66800000000"]
	for i in range(len(receive_account)):
		logging.info(receive_account[i])
		receive_account = np.array(receive_account)
		logging.info(receive_account[i])
		price = price[random.randint(0, len(price) - 1)]
		logging.info(price)
		logging.info("ra:{},reac{},pri{}".format(send_account, receive_account[i], price))
		try:
			api_params = [send_account, receive_account[i], price, "0x110", "0x30000", ""]
			logging.info("api_params:{} ".format(api_params))
			result = request_Api(api_name, api_params)
		# print("业务需求: 发送交易 transaction of 120,result:{}".format(result))
		except Exception as e:
			logging.info("随机发送多笔交易失败{}".format(e))
			continue
		return result


if __name__ == '__main__':
	log = apis.log.Logger(filename='../logs/transfer.log', level='info')
	api_name = "account_transfer"
	send_account = "0x00162F34533cB204868d619930188d38E49bC625"
	price = ["0x168000000000000", "0x18800000000", "0x16600000000", '0x1580000000', "0x368000000000", "0x66800000000"]
	receive_account = ca.create_account(api_name="account_createAccount", params=[])           #单个账号
	# receive_account = ca.create_account_100(peoples=3)  # 多个账号

	transaction_one(send_account, receive_account, price="0x18800000000")            #执行一笔交易
	# random_transaction(api_name, send_account, receive_account)
