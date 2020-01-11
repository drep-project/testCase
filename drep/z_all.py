#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from datetime import datetime
from time import sleep
import requests
import random


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
			print("creat_account_response:", response.text)
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
	
	def chain_getBalance(self, reciviceaccount):
		url = "http://127.0.0.1:15645"
		
		payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"chain_getBalance\",\n\t\"params\":[\"0xad3dc2d8aedef155eaba42ab72c1fe480699336c\"],\n\t\"id\": 3\n\t\n}\n"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "d191c48c-cef5-4a58-959f-9f487a41068e"
		}
		
		jsonDic = json.loads(payload)
		jsonDic["params"][0] = reciviceaccount
		print(jsonDic)
		payload = json.dumps(jsonDic)
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
		jsonDic = json.loads(response.text)  # 将json转换成python字典
		balance = jsonDic["result"]  # 从response中得到当前余额
		print("当前账户余额为:{}".format(balance))
		return balance
	
	def vote_credit(self):
		import requests
		
		url = "http://127.0.0.1:15645"
		
		payload = "{\n\t \t\"jsonrpc\":\"2.0\",\n\t \t\"method\":\"account_voteCredit\",\n\t \t\"params\":[\"0x45fdbcde02aad7a438052a7f4e74594c22245dd9\",\"0x75a45fb9e16b44e8c0b595d18c657f54b7300c3d\",\"0x111\",\"0x110\",\"0x30000\"],\n\t \t\"id\":1\n\t \t\n\t }\n"
		headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Postman-Token': "b47ba233-648b-49da-9328-0813b8f09f2b"
		}
		
		response = requests.request("POST", url, data=payload, headers=headers)
		
		print(response.text)
	
	
	
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
					print(
						datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易(收款账户) : " + account + "- 交易总次数{}".format(
							all_count))
					sleep(60)
					balance = self.chain_getBalance(account)
					print("当前账号为:{},该账号余额为:{}".format(account, balance))
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
