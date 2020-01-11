#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import random
import threading
from drep import api
from time import sleep
from drep.testcase import c_a as ca
# from .create_account import creat_account


# class myThread(threading.Thread):
#
# 	def __init__(self, threadID, rootAccount, account):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.rootAccount = rootAccount
# 		self.account = account
#
# 	def run(self):
# 		print("开始线程：" + str(self.threadID))
#
# 		# 实例
# 		# account = creat_account(peoples=1)
# 		# api.all_Api(account)
# 		sleep(600)
# 		# lock.release()
# 		print("退出线程：" + str(self.threadID))


# 执行 多次 transfer 函数


def Atransaction():
	count = 1
	
	rootAccount = ""
	recivice = creat_account.creat_account(peoples=100)
	price = ["0x168000000000000", "0x18800000000", "0x16600000000", '0x1580000000', "0x368000000000",
	         "0x66800000000"]
	
	response = api.all_Api(name="account_transfer",
	                       paramsa=[rootAccount, recivice, price[random.randint(0, len(price) - 1)],
	                                "0x110", "0x30000"])
	print(response)
	while True:
		# 永久运行
		if count > 120:
			count = 1
			sleep(3)
			continue
		try:
			global run, all_count
			rootAccount = ""
			recivice = creat_account(peoples=100)
			if run == 1:
				
				response = api.all_Api(name="account_transfer",
				                       paramsa=[rootAccount, recivice, price[random.randint(0, len(price) - 1)],
				                                "0x110", "0x30000"])
				print("发送者: {} --> 接收者: {}".format(rootAccount, recivice))
				print("api: {}  -- response: {}".format(recivice, response))
				all_count = all_count + 1
				print(
					datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 收款账户 : " + recivice + "- 交易总次数{}".format(
						all_count))
				sleep(60)
			else:
				print('暂停交易')
				sleep(30)
		# sleep(3)
		except Exception as e:
			print("交易失败!", e)
		count = count + 1
		print('执行一次交易休眠30s')
		sleep(30)

if __name__ == '__main__':
	# Atransaction(peoples=100)
	ca.creat_account(peoples=2)
	print(1)
