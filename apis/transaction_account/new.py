#!/usr/bin/env python
# encoding: utf-8
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
			transaction(self.a_list,self.b_list)
		
			print("退出线程：" + str(self.threadID))
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
			#print("resule",result)
			result = int(result["result"])
			if result > 100000:
				num_address_list.append(add)
			else:
				zero_address_list.append(add)
		except Exception as e:
			print("查询账户余额".format(e))
	print("num——address: {}".format(num_address_list))
	print("*"*10)
	print("zreo-address: {}".format(zero_address_list))

	return num_address_list, zero_address_list

def get_romod_add(add_list):
	'''
	
	:param add_list:
	:return:
	'''
	n = random.randint(0, len(add_list) - 1)
	return add_list[n]

def chain_jiaoyi(A_add, B_add,price):
	'''
	
	:param A_add:
	:param B_add:
	:param price:
	:return:
	'''
	params = [A_add, B_add, price, "0x110", "0x30000", ""]
	result = request_Api("account_transfer", params)
	return result

def get_address_list(api_name,param):
	'''
	得到系统中的当前所有账户地址
	:param api_name:
	:param param:
	:return:
	'''
	print("业务需求: 查询地址list account_listAddress")
	try:
		address = request_Api(api_name, param)
		#print(address)
		address_list = address["result"]
		#print("当前系统中所有地址为:{},共有{}个".format(address_list, len(address_list)))
	except Exception as e:
		return e  # 调用接口报错
	return address_list

def transaction(a_list, b_list):
	Send = get_romod_add(a_list)
	Accept = get_romod_add(b_list)
	r = chain_jiaoyi(Send, Accept, "0xa")
	print(r)
	print("{} ===> {}  【{}】".format(Send, Accept, "0xa"))
	


	


if __name__ == '__main__':
	all_address_list = get_address_list("account_listAddress", [])
	# print(a_address_list)
	a_list, b_list = getAB_list(all_address_list)
	a_list = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "0x391A25A3a9fE56ec4Ace616C4f864a1753604Ace",
				"0x21776E55F248f699E9Ae3a86c46Af9FCB372Fa5c", "0x720B6bDdad51aF100F365ee25C41cC356c1C10b9",
				"0x1B931e9924b6276747BffbDC69Ba6644b7B56a50", "0x30C2C948D77C79b0f38f729627Bb555f5e91c309",
				"0xba400Bc94a3d5Ba6A1386F5E9823878Eb3574A56", "0x45F04C0D5b8e71617cB989fD82852E5E14F284C0",
				"0xeece68A5EDae511Cb8F54A8BCd9AB9dD69A2F479", "0xF2Ec297aa634965046AE4B038794dBE2Cb9c7252",
				"0x3125a75c79DC3957627a26aCceA6085176f7AFD8", "0x55f68cFe462D607b239c6ca0259b4aA0274cB8C3",
				"0xAD0Af35Ad0549c4C1ead4BedDFa26a036a30E6cA", "0x57eA6795dE2C671fCa9F044831E899668FEd7933",
				"0x6057Dabf49FEC23d3176F05567907c0e77D4eDA7", "0xf7A3908EF49F519aecDc1d48e1B165EF8e83b62D",
				"0x46B8E9685Aa677637922596607b509eBF751E459", "0x8514b8Dc105586335C951E2B7f908DDFF71C3c7F",
				"0x3a8A75397C6e9Db63f01b91187010190076b7C77", "0x4A721122a3E85BB9B63fC480340A14cfED734a33",
				"0xe5B44f6b865A1ab4584C645AC8cB86B0f7166048", "0x3349f91486E227dF367dEb02fF8cD3144b04E09e"]
	nums = 1000
	j = 0
	while j < nums:
		# 创建两个线程
		try:
			# 创建新线程
			thread = myThread(j, a_list, b_list)
			thread.start()
			#thread2 = myThread(2, "Thread-2", 2).start()
			# 开启新线程
			thread.join()
			#thread2.join()
			print("退出主线程")

		except:
			print("Error: 无法启动线程")
		j = j+1
