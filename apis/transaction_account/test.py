import logging


from transaction_account.API import save_excel
from Utils import *
from transaction_account.api_get_addresslist import get_address_list
from transaction_account.API import request_Api
from transaction_account.api_chain_transaction import transaction_one, random_transaction

# !/usr/bin/env python
# encoding: utf-8
from transaction_account.unlock_account import unlockAccount

'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: new.py
@time: 2020/2/25 11:16 pm
@desc:
'''
import threading

from transaction_account.API import request_Api
import random


class myThread(threading.Thread):
	
	def __init__(self, threadID, a_list, b_list):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.a_list = a_list
		self.b_list = b_list
	
	def run(self):
		print("开始线程：" + str(self.threadID))
		# 实例
		while True:
			transaction(self.a_list, self.b_list)
			print("退出线程：" + str(self.threadID))


def open_excel(file='test2.xlsx'):
	'''打开文件'''
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print(e)

def excel_table_byindex(file='test2.xlsx', colnameindex=0, by_index=0):
	'''
	 根据索引获取Excel表格中的数据
	:param file: Excel文件路径
	:param colnameindex:   表头列名所在行的索引
	:param by_index:  表的索引
	:return: 表中的数据
	'''
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows  # 行数
	# ncols = table.ncols #列数
	colnames = table.row_values(colnameindex)  # 某一行数据
	app_list = []
	for rownum in range(1, nrows):
		
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			app_list.append(app)
	return app_list

def send_excel_account():
	'''
	新创建账号
	读取表中的地址并对新创建的脏那港澳发起交易
	:return:表中的地址
	'''
	tables = excel_table_byindex()
	print("表中的数据{}".format(tables))
	send_account_list = []
	for row in tables:
		print("账号为", row["余额不为零的账号"])  # 读取字典中key的值为“余额不为零的账号”的数据
		unlockAccount("account_unlockAccount", [row["余额不为零的账号"]])       # 解锁excel中的账号地址
		send_account_list.append(row["余额不为零的账号"])
	return send_account_list

def getAB_list(all_list):
	'''

	:param all_list:
	:return:
	'''
	num_address_list = []
	zero_address_list = []
	for add in all_list:
		try:
			result = request_Api("chain_getBalance", [add])
			# print("resule",result)
			result = int(result["result"])
			if result > 100000:
				unlockAccount("account_unlockAccount", [add])
				num_address_list.append(add)
			else:
				zero_address_list.append(add)
		except Exception as e:
			print("查询账户余额".format(e))
	print("num——address: {}".format(num_address_list))
	print("*" * 10)
	print("zreo-address: {}".format(zero_address_list))
	
	return num_address_list, zero_address_list


def get_romod_add(add_list):
	'''

	:param add_list:
	:return:
	'''
	n = random.randint(0, len(add_list) - 1)
	return add_list[n]


def chain_transaction(A_add, B_add, price):
	'''
	发送交易
	:param A_add:发地址
	:param B_add:收地址
	:param price:金额
	:return:
	'''
	params = [A_add, B_add, price, "0x110", "0x30000", ""]
	result = request_Api("account_transfer", params)
	return result


def get_address_list(api_name, param):
	'''
	得到系统中的当前所有账户地址
	:param api_name:
	:param param:
	:return:
	'''
	print("业务需求: 查询地址list account_listAddress")
	try:
		address = request_Api(api_name, param)
		# print(address)
		address_list = address["result"]
	# print("当前系统中所有地址为:{},共有{}个".format(address_list, len(address_list)))
	except Exception as e:
		return e  # 调用接口报错
	return address_list


def transaction(a_list, b_list):
	Send = get_romod_add(a_list)
	Accept = get_romod_add(b_list)
	re = chain_transaction(Send, Accept, "0xa")
	print("交易结果：{}".format(re))
	print("{} ===> {}  【{}】".format(Send, Accept, "0xa"))


if __name__ == '__main__':
	all_address_list = get_address_list("account_listAddress", [])
	print(all_address_list)
	a_list, b_list = getAB_list(all_address_list[0:10])
	a_list = send_excel_account()
	print(a_list)
	nums = 600
	j = 0
	while j < nums:
		# 创建两个线程
		try:
			# 创建新线程
			thread = myThread(j, a_list, b_list)
			thread.start()
			# thread2 = myThread(2, "Thread-2", 2).start()
			# 开启新线程
			thread.join()
			# thread2.join()
			print("退出主线程")
		
		except:
			print("Error: 无法启动线程")
		j = j + 1


# def chain_getBalance(api_name, params):
# 	'''
#
# 	:return: 查询对应账户的余额
# 	'''
# 	logging.info("业务  请求 chain_getBalance")
# 	try:
# 		result = request_Api(api_name, params)
# 		result = result["result"]
# 		logging.info(result)
# 	except:
# 		logging.error("查询余额失败,{}".format(result))
# 		return result
# 	return result
#
#
# def getBalance_of_all_address_list(api_name, address):
# 	'''
# 	返回所有余额不为0的账号与账户余额
# 	:param api_name:
# 	:param address:
# 	:return:返回所有余额不为0的账号与账户余额
# 	'''
# 	result_list = []  # 余额list
# 	getBalance_account_list = []  # 余额不为0的账号list
#
# 	for i in range(len(address)):
# 		# if i == 100000:
# 		# 	break
# 		params = [address[i]]
# 		try:
# 			result = request_Api(api_name, params)
# 		except Exception as e:
# 			logging.error("查询地址中所有账号余额失败,{}".format(e))
# 			continue
# 		logging.info("业务请求: {},result:{}".format(api_name, result))
# 		print("查询账号: {},查询结果: {}".format(params, result))
#
# 		result = int(result["result"])
#
# 		#print(result)
# 		#result = int(result / pow(10, 18))
# 		#print("除以18后{}".format(result))
#
# 		if result != 666666:
# 			print("比较后{}".format(result))
# 			result_list.append(result)
# 			#print("比较后{}".format(result_list))
# 			getBalance_account_list.append(params)
# 		else:
# 			logging.info("结果为:{}".format(result))
# 	logging.info("有余额的账户为:{},共有{}余额".format(getBalance_account_list, result_list))
# 	print(getBalance_account_list, getBalance_account_list)
# 	return getBalance_account_list, result_list
#
#
# def transfer_balance(api_name, send_account, receive_account, price):
# 	'''
# 		执行一笔交易前查询余额,执行一笔交易之后,再次查询余额进行对比
# 	:param api_name:
# 	:param send_account:
# 	:param receive_account:
# 	:param price:
# 	:return:
# 	'''
# 	send_account_balance_before = chain_getBalance(api_name, [send_account]) # 查询发送交易之前发送账号的余额,并得到result中的值
# 	receive_account_balance_before = chain_getBalance(api_name, [receive_account])  # 查询发送交易之前接收交易的账号的余额
# 	print("send_account发送前账号: {},send_account发送前余额: {},received_account接收账号之前账号：{},received_account接收账号之前余额: {}"
# 	      .format(send_account, send_account_balance_before,receive_account, receive_account_balance_before))
# 	result = transaction_one(send_account, receive_account, price)  # 发送一笔交易
# 	print("发送一笔交易", result)
# 	result = {
# 		"send_account": send_account,
# 		"receive_account": receive_account,
# 		"price": price,
# 		"send_account_balance_before": send_account_balance_before,
# 		"receive_account_balance_before": receive_account_balance_before
# 	}
# 	# 写入 Excel  Utils
# 	excel_write('./before_price.xls', [
# 		['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before',
# 		 'receive_account_balance_before'],
# 		[result.get("send_account"), result.get("receive_account"), result.get("price"),
# 		 result.get("send_account_balance_before"),
# 		 result.get("receive_account_balance_before")],
# 		[result.get("send_account"), result.get("receive_account"), result.get("price"),
# 		 result.get("send_account_balance_before"),
# 		 result.get("receive_account_balance_before")]
# 	])
# 	return result
#
#
# def check_transfer_balance(api_name):
# 	'''
# 	查询交易后账户余额
# 	:param api_name:
# 	:return:
# 	'''
# 	# 读Excel 文件
# 	results = excel_read_dict('before_price.xls')
# 	print(results)
# 	# api_name = "chain_getBalance"
# 	for result in results:
# 		send_account_balance_after = chain_getBalance(api_name, [result["send_account"]])["result"]  # 查询发送交易之前发送账号的余额
# 		receive_account_balance_after = chain_getBalance(api_name, [result["receive_account"]])[
# 			"result"]  # 查询发送交易之前接收交易的账号的余额
#
# 		print("send_account发送账号发送后余额,{},received_account接收账号之后余额{}".format(send_account_balance_after,
# 		                                                                   receive_account_balance_after))
# 		result["send_account_balance_after"] = send_account_balance_after
# 		result["receive_account_balance_after"] = receive_account_balance_after
#
#
# 	excel_write('./after_price.xls', [
# 		['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before',
# 		 'receive_account_balance_before',
# 		 'send_account_balance_after', 'receive_account_balance_after'],
# 		[result.get("send_account"), result.get("receive_account"),
# 		 result.get("transfer_price"), result.get("send_account_balance_before"),
# 		 result.get("receive_account_balance_before"),
# 		 result.get("send_account_balance_after"),
# 		 result.get("receive_account_balance_after")],
# 		[result.get("send_account"), result.get("receive_account"),
# 		 result.get("transfer_price"),
# 		 result.get("send_account_balance_before"),
# 		 result.get("receive_account_balance_before"),
# 		 result.get("send_account_balance_after"),
# 		 result.get("receive_account_balance_after")]
# 	])
#
#
# if __name__ == '__main__':
# 	# log = apis.log.Logger(filename='../logs/getBalance.log', level='debug')
# 	address_list = get_address_list(api_name="account_listAddress", param=[])
# 	logging.info("传入地址为:{}".format(address_list))
# 	# print(address_list)
# 	# address_list = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0"]
# 	account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)
# 	name = u'余额不为零的账号'
# 	money = u'金额'
# 	save_excel(account, result, name, money, "test")  # 生成Excel
#
