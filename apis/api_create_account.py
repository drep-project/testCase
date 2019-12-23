import json
from time import sleep
from apis.API import request_Api


def create_account(api_name, params):
	"""
	主业务函数   创建单账户
	:return:
	"""
	people = 1
	print("业务需求: 创建一个账户 account_createAccount")
	result = request_Api(api_name, params)
	result = result["result"]
	return result


def create_account_100(peoples=100):
	"""
	主业务函数   创建100账户
	:return:
	"""
	
	api_name = "account_createAccount"
	params = []
	
	account_all = []
	for i in range(peoples):
		# 用户 xxx
		try:
			response = request_Api(api_name, params)
			print("创建用户：", response)
			result = response["result"]
			# sleep(2)
			account_all.append(result)
		except Exception as e:
			print("账户创建失败!")
			sleep(3)
			print("账户创建失败!")
	print(account_all)
	return account_all


if __name__ == '__main__':
	api_name = "account_createAccount"
	params = []
	create_account_100(3)
