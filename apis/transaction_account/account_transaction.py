#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_transaction.py
@time: 2020/2/21 6:07 pm
@desc:
'''
import _thread
import threading
import time
import xdrlib, sys
import xlrd

from creat_account.api_get_addresslist import get_address_list
from transaction_account.API import save_excel
from transaction_account.api_chain_getBalance import getBalance_of_all_address_list, check_transfer_balance
from transaction_account.api_create_account import create_account
from transaction_account.unlock_account import unlockAccount
from transaction_account.api_chain_getBalance import transfer_balance


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
	list = []
	for rownum in range(1, nrows):
		
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	return list


'''
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称

def excel_table_byname(file= '余额不为0的账号.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list
'''


def main():
	'''
	新创建账号
	读取表中的地址并对新创建的脏那港澳发起交易
	:return:表中的地址
	'''
	tables = excel_table_byindex()
	print("表中的数据{}".format(tables))
	#root_account_list = []
	for row in tables:
		print("账号为", row["余额不为零的账号"])  # 读取字典中key的值为“余额不为零的账号”的数据
		#root_account_list.append()
		#unlockAccount("account_unlockAccount", row["余额不为零的账号"])       # 解锁excel中的账号地址
		transfer_balance("chain_getBalance", row["余额不为零的账号"], create_account("account_createAccount", []), "0xa")       # 使用excel中的账号对新创建的地址发送交易
		
		#return row["余额不为零的账号"]

class myThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		# self.name = name
		# self.counter = counter
	def run(self):
		print("开始线程：" + self.name)
		while True:
			main()
			print("退出线程：" + self.name)
	
def transation20():
	'''
	读取excel中地址并新创建地址发送交易，共执行20次
	:return:
	'''
	nums = 100
	j = 0
	while j < nums:
		# 创建两个线程
		try:
			# 创建新线程
			thread = myThread(j)
			thread.start()
			#thread2 = myThread(2, "Thread-2", 2).start()
			# 开启新线程
			thread.join()
			#thread2.join()
			print("退出主线程")

		except:
			print("Error: 无法启动线程")
		j = j+1
	


'''
   # tables = excel_table_byname()
   # for row in tables:
   #     print(row)
'''

if __name__ == "__main__":
	# while True:
	# 	address_list = get_address_list(api_name="account_listAddress", param=[])  # 得到系统中的所有地址
	# 	all_account, result = getBalance_of_all_address_list(api_name="chain_getBalance",
	# 	                                                     address=address_list)  # 得到余额的18次方大约0的所有地址
	# 	name = u'余额不为零的账号'
	# 	money = u'金额'
	# 	save_excel(all_account, result, name, money, "余额不为0的账号")  # 生成Excel
		transation20()
		time.sleep(60)
		check_transfer_balance("chain_getBalance")
	
		
		
	
