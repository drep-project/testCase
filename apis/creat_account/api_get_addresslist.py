import logging
import log
from transaction_account import API as api

log.Logger(filename="get_addresslist.log")


def get_address_list(api_name, param):
	'''
	得到系统中的当前所有账户地址
	:param api_name:
	:param param:
	:return:
	'''
	print("业务需求: 查询地址list account_listAddress")
	try:
		address = api.request_Api(api_name, param)
		print(address)
		address_list = address["result"]
		print("当前系统中所有地址为:{},共有{}个".format(address_list, len(address_list)))
	except Exception as e:
		logging.info("查询系统中所有地址报错{}".format(e))
		return -1  # 调用接口报错
	return address_list


if __name__ == '__main__':
	api_name = "account_listAddress"
	param = []
	get_address_list(api_name, param)
