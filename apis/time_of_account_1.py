#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from datetime import datetime
from time import sleep
from apis.api_chain_transaction import *
from apis.api_create_account import create_account_100


def transation_120_account_1(sendaccount, account):
	'''
	一个账号执行120次交易
	:param sendaccount: 发送者
	:param account: 接受者
	:return: 返回一个账户执行120次后的120个结果数组
	'''
	transaction_120_resule = []
	for i in range(120):
		t = transaction_one(sendaccount, account)
		transaction_120_resule.append(t)
		print(i)
	return transaction_120_resule




def transations_120_account_many(send_account,received_account):
	count = 1
	while True:
		# 永久运行
		if count > 120:
			count = 1
			sleep(3)
			continue
		try:
			global run, all_count
			if run == 1:
				print("发送者: {} --> 接收者: {}".format(send_account, received_account))
				response = random_transaction()
				print("api: {}  -- response: {}".format(received_account, response))
				all_count = all_count + 1
				print(
					datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 收款账户 : " + received_account + "- 交易总次数{}".format(all_count))
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
# 		#实例
# 		random_transaction(peoples=1)
# 		sleep(600)
# 		print("退出线程：" + str(self.threadID))

# 执行 120次 交易 函数


if __name__ == '__main__':
	send_account = "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"
	received_account = create_account_100(peoples=100)
	transations_120_account_many(send_account, received_account)
	print(received_account)