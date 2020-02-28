import logging


from transaction_account.API import save_excel
from Utils import *
from transaction_account.api_get_addresslist import get_address_list
from transaction_account.API import request_Api
from transaction_account.api_chain_transaction import transaction_one, random_transaction


def chain_getBalance(api_name, params):
	'''
	
	:return: 查询对应账户的余额
	'''
	logging.info("业务  请求 chain_getBalance")
	try:
		result = request_Api(api_name, params)
		result = result["result"]
		logging.info(result)
	except:
		logging.error("查询余额失败,{}".format(result))
		return result
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
		print("查询账号: {},查询结果: {}".format(params, result))
		
		result = int(result["result"])
		
		#print(result)
		#result = int(result / pow(10, 18))
		#print("除以18后{}".format(result))
		
		if result > 0:
			print("比较后{}".format(result))
			result_list.append(result)
			#print("比较后{}".format(result_list))
			getBalance_account_list.append(params)
		else:
			logging.info("结果为:{}".format(result))
	logging.info("有余额的账户为:{},共有{}余额".format(getBalance_account_list, result_list))
	print(getBalance_account_list, getBalance_account_list)
	return getBalance_account_list, result_list


def transfer_balance(api_name, send_account, receive_account, price):
	'''
		执行一笔交易前查询余额,执行一笔交易之后,再次查询余额进行对比
	:param api_name:
	:param send_account:
	:param receive_account:
	:param price:
	:return:
	'''
	send_account_balance_before = chain_getBalance(api_name, [send_account]) # 查询发送交易之前发送账号的余额,并得到result中的值
	receive_account_balance_before = chain_getBalance(api_name, [receive_account])  # 查询发送交易之前接收交易的账号的余额
	print("send_account发送前账号: {},send_account发送前余额: {},received_account接收账号之前账号：{},received_account接收账号之前余额: {}"
	      .format(send_account, send_account_balance_before,receive_account, receive_account_balance_before))
	result = transaction_one(send_account, receive_account, price)  # 发送一笔交易
	print("发送一笔交易", result)
	result = {
		"send_account": send_account,
		"receive_account": receive_account,
		"price": price,
		"send_account_balance_before": send_account_balance_before,
		"receive_account_balance_before": receive_account_balance_before
	}
	# 写入 Excel  Utils
	excel_write('./before_price.xls', [
		['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before',
		 'receive_account_balance_before'],
		[result.get("send_account"), result.get("receive_account"), result.get("price"),
		 result.get("send_account_balance_before"),
		 result.get("receive_account_balance_before")],
		[result.get("send_account"), result.get("receive_account"), result.get("price"),
		 result.get("send_account_balance_before"),
		 result.get("receive_account_balance_before")]
	])
	return result


def check_transfer_balance(api_name):
	'''
	查询交易后账户余额
	:param api_name:
	:return:
	'''
	# 读Excel 文件
	results = excel_read_dict('before_price.xls')
	print(results)
	# api_name = "chain_getBalance"
	for result in results:
		send_account_balance_after = chain_getBalance(api_name, [result["send_account"]])["result"]  # 查询发送交易之前发送账号的余额
		receive_account_balance_after = chain_getBalance(api_name, [result["receive_account"]])[
			"result"]  # 查询发送交易之前接收交易的账号的余额
		
		print("send_account发送账号发送后余额,{},received_account接收账号之后余额{}".format(send_account_balance_after,
		                                                                   receive_account_balance_after))
		result["send_account_balance_after"] = send_account_balance_after
		result["receive_account_balance_after"] = receive_account_balance_after

	
	excel_write('./after_price.xls', [
		['send_account', 'receive_account', 'transfer_price', 'send_account_balance_before',
		 'receive_account_balance_before',
		 'send_account_balance_after', 'receive_account_balance_after'],
		[result.get("send_account"), result.get("receive_account"),
		 result.get("transfer_price"), result.get("send_account_balance_before"),
		 result.get("receive_account_balance_before"),
		 result.get("send_account_balance_after"),
		 result.get("receive_account_balance_after")],
		[result.get("send_account"), result.get("receive_account"),
		 result.get("transfer_price"),
		 result.get("send_account_balance_before"),
		 result.get("receive_account_balance_before"),
		 result.get("send_account_balance_after"),
		 result.get("receive_account_balance_after")]
	])


if __name__ == '__main__':
	# log = apis.log.Logger(filename='../logs/getBalance.log', level='debug')
	address_list = get_address_list(api_name="account_listAddress", param=[])
	logging.info("传入地址为:{}".format(address_list))
	# print(address_list)
	# address_list = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0"]
	account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)
	name = u'余额不为零的账号'
	money = u'金额'
	save_excel(account, result, name, money, "余额不为0的账号")  # 生成Excel
	
	
	
	
	
	'''
	
api_name = "chain_getBalance"
account = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "0x016fA969d48C0BeB39e099d88356500Be5b854f3"]
price = "0xf4240"
transfer_balance(api_name, account[0], account[1], price)
time.sleep(180)
check_transfer_balance(api_name)
rootaccount = 0xad3dc2d8aedef155eaba42ab72c1fe480699336c
result = transaction_one(send_account="0x6C92Dfe1059e66517dFC2126A90C204c95F511ef", receive_account=address_list,
                         price="186a0")  # 执行多次交易
logging.info("执行多次交易.{}".format(result))
account, result = getBalance_of_all_address_list(api_name="chain_getBalance", address=address_list)  # 再次查看余额
name = u'余额不为零的账号'
money = u'金额'
save_excel(account, result, name, money, "执行多次交易后的余额")

	'''
