from apis.API import request_Api  # 必须导入  用于向后端发送请求
from apis.api_get_addresslist import get_address_list as address
from apis.api_chain_transaction import *
from apis.API import save_excel
import logging
import apis.log



def chain_getBalance(api_name, params):
	'''
	
	:return: 查询对应账户的余额
	'''
	logging.info("业务  请求 chain_getBalance")
	try:
		result = request_Api(api_name, params)
		logging.info(result)
	except Exception as e:
		logging.error("查询余额失败,{}".format(e))
		return -1
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
		try:
			result = request_Api(api_name, params)
		except Exception as e:
			logging.error("查询地址中所有账号余额失败,{}".format(e))
			continue
		logging.info("业务请求: {},result:{}".format(api_name, result))
		result = result["result"]
		if result > 0:
			result_list.append(result)
			getBalance_account_list.append(params)
		else:
			logging.info("结果为:{}".format(result))
	logging.info("有余额的账户为:{},共有{}余额".format(getBalance_account_list, result_list))
	return getBalance_account_list, result_list


# 转账
# 查余额
# 转账100笔
# 查余额
# transaction_one("0x2777fcb6365b64876be85fbfe5e0242ec8852157", "0x712f455a6102987450c2daade60d3f1c8b3b551d")

if __name__ == '__main__':
	log = apis.log.Logger(filename='../logs/getBalance.log', level='debug')
	address_list = address(api_name="account_listAddress", param=[])
	logging.info("传入地址为:{}".format(address_list))
	account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)
	name = u'余额不为零的账号'
	money = u'金额'
	save_excel(account, result, name, money, "余额不为0的账号及金额")  # 生成Excel
	# rootaccount=0xad3dc2d8aedef155eaba42ab72c1fe480699336c
	result = transaction_one(send_account="0x6C92Dfe1059e66517dFC2126A90C204c95F511ef", receive_account=address_list,
	                         price="186a0")  # 执行多次交易
	logging.info("执行多次交易.{}".format(result))
	account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)  # 再次查看余额
	name = u'余额不为零的账号'
	money = u'金额'
	save_excel(account, result, name, money, "执行多次交易后的余额")
