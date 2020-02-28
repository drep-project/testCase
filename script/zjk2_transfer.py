#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: zjk2_transfer.py
@time: 2020/1/1 4:59 下午
@desc:
'''
import json
import logging
import threading
from datetime import datetime
from time import sleep
import requests
import random
import time


class myThread(threading.Thread):
	
	def __init__(self, threadID, rootAccount, account):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.rootAccount = rootAccount
		self.account = account
	
	def run(self):
		logging.info("开始线程：" + str(self.threadID))
		print("开始线程：" + str(self.threadID))
		# 一个账户执行 120次
		
		# 实例
		api = Api(self.rootAccount)
		api.times_of_120(self.account)
		# sleep(600) 休眠600/ times_of_120中的sleep(30) 等于1m执行20个
		print("退出线程：" + str(self.threadID))
		logging.info("退出线程：" + str(self.threadID))


class Api():
	'''

	'''
	
	def __init__(self, rootAccount):
		i = random.randint(0, len(rootAccount) - 1)
		self.rootAccount = rootAccount[i]
	
	# 创建账户
	def creat_account(self):
		# url = "http://47.75.98.179:15645"
		
		url = "http://39.98.39.224:35645"
		
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_createAccount\",\n\t\"params\":[], \n\t\"id\": 3\n\t\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
		}
		try:
			response = requests.request("POST", url, data=payload, headers=headers)
			logging.info("creat_account_response:{}".format(response.text))
			print("creat_account_response:{}".format(response.text))
			jsonDic = json.loads(response.text)
			print("创建账户:" + jsonDic['result'])
			return jsonDic['result']
		except Exception as e:
			logging.error("HTTP error".format(e))
			print("HTTP error".format(e))
			return "error Account", e
	
	# 发交易  0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c
	def privkey_api(self, count, rootAccount, recivice):
		logging.info("发送者: {} --> 接收者: {}".format(rootAccount, recivice))
		print("发送者: {} --> 接收者: {}".format(rootAccount, recivice))
		
		# url = "http://47.75.98.179:15645"
		url = "http://39.98.39.224:35645"
		
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_transfer\",\n\t\"params\":[\"0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c\",\"0xde4541def39ca2393d159f6f407d225dfb653c22\",\"0x16800000000\",\"0x110\",\"0x30000\",\"\"],\n\t\"id\":1\n\t\n}"
		jsonDic = json.loads(payload)
		# print(jsonDic)
		jsonDic["params"][0] = rootAccount
		jsonDic["params"][1] = recivice
		price = ["0x168000000000000", "0x18800000000", "0x16600000000", '0x1580000000', "0x368000000000",
		         "0x66800000000"]
		jsonDic["params"][2] = price[random.randint(0, len(price) - 1)]
		payload = json.dumps(jsonDic)
		logging.info("recivice_account: {}  -- data: {}".format(recivice, payload))
		
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "6616a7d2-3705-4d37-b779-ef595abde465"
		}
		# print('******start*****************')
		response = requests.request("POST", url, data=payload, headers=headers)
		logging.info('privkey_response: {}'.format(response.text))
		print('privkey_response: {}'.format(response.text))
		
		return response.text
	
	def check_block(self):
		url = "http://47.75.98.179:15645"
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"chain_getMaxHeight\",\n\t\"params\":[],\n\t\"id\":1\n\t\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "d3e4e378-5f3f-4318-afb7-88842840f014"
		}
		try:
			response = requests.request("POST", url, data=payload, headers=headers)
			logging.info("目前api区块高度为{}".format(response.text))
			print("目前api区块高度为{}".format(response.text))
			jsonDic = json.loads(response.text)  # 将json转换成python字典
			logging.info("将json转换成python字典{}".format(jsonDic))
			# print("将json转换成python字典{}".format(jsonDic))
			block_hight = jsonDic["result"]  # 从response中得到当前区块高度
			# print("当前区块高度为:{}".format(block_hight))
			return block_hight
		except Exception as e:
			logging.error("获得区块高度错误{}".format(e))
			print(e)
			return -1
	
	# 执行 120次 transfer 函数
	def times_of_120(self, account):
		count = 1
		while True:
			# 单次运行
			# if count > 120:
			# 	break
			
			# 永久运行
			if count > 120:
				count = 1
				sleep(3)
				continue
			try:
				global run, all_count
				if run == 1:
					# print("root", self.rootAccount)
					# print("acc", account)
					self.privkey_api(count, self.rootAccount, account)
					all_count = all_count + 1
					logging.info(
						datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易(收款账户) : " + account + "- 交易总次数{}".format(
							all_count))
				# sleep(6)  #60
				else:
					logging.info('暂停交易')
			# sleep(3)       #30
			# sleep(3)
			except Exception as e:
				print("交易失败!".format(e))
				logging.error("交易失败!".format(e))
			count = count + 1
			logging.info('执行一次交易休眠30s')
			print('执行一次交易休眠30s')


# sleep(30)  #休眠600/ times_of_120中的sleep(30) 等于1m执行20个


# 单个账户发送 120 次交易
# times_of_120(account)
# 100个独立账户运行
def account_100_run_pay_120(peoples=100):
	# 实例
	global rootAccount
	api = Api(rootAccount)
	# account_100 = []
	for i in range(peoples):
		# 用户 xxx
		try:
			account = api.creat_account()
			# 为一个用户创建一个线程 独立运行 120 次交易
			logging.info("创建用户： {}".format(i) + account)
			print("创建用户： {}".format(i) + account)
			# times_of_120(account)
			# account_100.append(account)
			threadX = myThread(i, rootAccount, account)
			threadX.start()
		# sleep(2)
		except Exception as e:
			print("账户创建失败!".format(e))
			logging.error("账户创建失败!".format(e))
			sleep(3)


# 每n秒执行一次
def timer(n):
	global run, height, rootAccount
	api = Api(rootAccount)
	
	while True:
		account_100_run_pay_120(100000)
		heightNew = api.check_block()
		localtime = time.asctime(time.localtime(time.time()))  # 得到本地时间
		# print("本地时间为:{},区块高度: {}".format(localtime, heightNew))
		if height == heightNew:
			run = 0
			logging.error("高度相同,停止交易".format(heightNew))
		else:
			height = heightNew
			run = 1
		time.sleep(n)
		# print(run, height)
		print("本地时间为:{},区块高度: {},run:{}".format(localtime, heightNew, run))
		logging.info("本地时间为:{},区块高度: {},run:{}".format(localtime, heightNew, run))


if __name__ == '__main__':
	run = 1
	height = 0
	all_count = 0
	# rootAccount = ["0x00dDEd572F4b40AA36a38FdC9c0aD7A7D483e94B", "0x00CA900E4aaE2123ADBb788222d4974B4db54D47",
	#                "0x00c4A24F2A38d325bcc43A7b338be2125784d6aC", "0x00bB8Deff193Fec9594Fa65DC3955105534E9654",
	#                "0x00b30D39C719aEC376e5b2C48bE6Ef17174aF479", "0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
	rootAccount = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]

	timer(60)

