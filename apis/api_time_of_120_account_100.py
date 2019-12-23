#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import threading
from datetime import datetime
from time import sleep
import requests
import random
import time
from threading import Lock, Thread


class myThread(threading.Thread):
	
	def __init__(self, threadID, rootAccount, account):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.rootAccount = rootAccount
		self.account = account
	
	def run(self):
		print("开始线程：" + str(self.threadID))
		# 一个账户执行 120次
		# lock = Lock()
		# lock.acquire()
		
		# 实例
		api = Api(self.rootAccount)
		api.times_of_120(self.account)
		sleep(600)
		# lock.release()
		print("退出线程：" + str(self.threadID))


class Api():
	def __init__(self, rootAccount):
		i = random.randint(0, len(rootAccount) - 1)
		self.rootAccount = rootAccount[i]
	
	# 创建账户
	def creat_account(self):
		url = "http://127.0.0.1:15645"
		
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_createAccount\",\n\t\"params\":[], \n\t\"id\": 3\n\t\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
		}
		try:
			response = requests.request("POST", url, data=payload, headers=headers)
			print("creat_account_response:{}", response.text)
			jsonDic = json.loads(response.text)
			# print("创建账户:" + jsonDic['result'])
			# print("num: {}".format(num))
			return jsonDic['result']
		except:
			print("HTTP error")
			return "error Account"
	
	# 发交易  0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c
	def privkey_api(self, count, rootAccount, recivice):
		print("发送者: {} --> 接收者: {}".format(rootAccount, recivice))
		url = "http://127.0.0.1:15645"
		
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_transfer\",\n\t\"params\":[\"0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c\",\"0xde4541def39ca2393d159f6f407d225dfb653c22\",\"0x16800000000\",\"0x110\",\"0x30000\",\"\"],\n\t\"id\":1\n\t\n}"
		jsonDic = json.loads(payload)
		# print(jsonDic)
		jsonDic["params"][0] = rootAccount
		jsonDic["params"][1] = recivice
		price = ["0x168000000000000", "0x18800000000", "0x16600000000", '0x1580000000', "0x368000000000",
		         "0x66800000000"]
		jsonDic["params"][2] = price[random.randint(0, len(price) - 1)]
		payload = json.dumps(jsonDic)
		print("recivice_account: {}  -- data: {}".format(recivice, payload))
		
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "6616a7d2-3705-4d37-b779-ef595abde465"
		}
		# print('******start*****************')
		response = requests.request("POST", url, data=payload, headers=headers)
		print('privkey_response: ' + response.text)
		return response.text
	
	def check_block(self):
		url = "http://127.0.0.1:15645"
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"chain_getMaxHeight\",\n\t\"params\":[],\n\t\"id\":1\n\t\n}"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "d3e4e378-5f3f-4318-afb7-88842840f014"
		}
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
		jsonDic = json.loads(response.text)  # 将json转换成python字典
		print(jsonDic)
		block_hight = jsonDic["result"]  # 从response中得到当前区块高度
		return block_hight
	
	# 执行 120次 交易 函数
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
					print(
						datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易(收款账户) : " + account + "- 交易总次数{}".format(
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
			print("创建用户： {}".format(i) + account)
			# times_of_120(account)
			# account_100.append(account)
			threadX = myThread(i, rootAccount, account)
			threadX.start()
		# sleep(2)
		except Exception as e:
			print("账户创建失败!")
			sleep(3)
			print("账户创建失败!")


# 每n秒执行一次
def timer(n):
	global run, height, rootAccount
	api = Api(rootAccount)
	
	while True:
		account_100_run_pay_120(100)
		heightNew = api.check_block()
		localtime = time.asctime(time.localtime(time.time()))  # 得到本地时间
		# print("本地时间为:{},区块高度: {}".format(localtime, heightNew))
		if height == heightNew:
			run = 0
			print("高度相同,停止交易")
		else:
			height = heightNew
			run = 1
		time.sleep(n)
		# print(run, height)
		print("本地时间为:{},区块高度: {},run:{}".format(localtime, heightNew, run))


run = 1
height = 0
all_count = 0
rootAccount = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
timer(60)
