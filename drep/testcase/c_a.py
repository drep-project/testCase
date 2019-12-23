#!/usr/bin/python
# -*- coding: UTF-8 -*-

from drep import api
from time import sleep

'''创建账号'''


def creat_account(peoples=100):
	account_all = []
	for i in range(peoples):
		# 用户 xxx
		try:
			response, account = api.all_Api(name="account_createAccount", paramsa=[])
			print("创建用户：{}".format(i) + account)
			# sleep(2)
			account_all.append(account)
		except Exception as e:
			print("账户创建失败!")
			sleep(3)
			print("账户创建失败!")
	return account_all


if __name__ == '__main__':
	account = []
	acc = creat_account(peoples=100)
	account.append(acc)
	print(account)
