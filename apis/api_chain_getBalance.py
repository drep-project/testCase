from apis.API import request_Api  # 必须导入  用于向后端发送请求
from apis.api_get_addresslist import get_address_list as address
from apis.api_chain_transaction import *
from apis.API import save_excel


def chain_getBalance(api_name, params):
	'''
	
	:return: 查询对应账户的余额
	'''
	print("业务  请求 chain_getBalance")
	result = request_Api(api_name, params)
	print(result)
	
	return result


def getBalance_of_all_address_list(api_name, address):
	'''
	返回所有余额不为0的账号与账户余额
	:param api_name:
	:param address:
	:return:返回所有余额不为0的账号与账户余额
	'''
	result_list = []  # 余额list
	getBalance_account_list = []  # 余额不为0的账号list
	for i in range(len(address)):
		params = [address[i]]
		result = request_Api(api_name, params)
		print("业务请求: {},result:{}".format(api_name, result))
		result = result["result"]
		if result > 0:
			result_list.append(result)
			getBalance_account_list.append(params)
		else:
			print("结果为:{}".format(result))
	print("有余额的账户为:{},共有{}余额".format(getBalance_account_list, result_list))
	return getBalance_account_list, result_list


# 转账
# 查余额
# 转账100笔
# 查余额
# transaction_one("0x2777fcb6365b64876be85fbfe5e0242ec8852157", "0x712f455a6102987450c2daade60d3f1c8b3b551d")

if __name__ == '__main__':
	address_list = address(api_name="account_listAddress", param=[])
	print("传入地址为:", address_list)
	account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)
	name = u'余额不为零的账号'
	money = u'金额'
	save_excel(account, result, name, money, "余额不为0的账号及金额3")
