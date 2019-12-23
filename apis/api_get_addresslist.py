from apis import API as api


def get_address_list(api_name, param):
	'''
	得到系统中的当前所有账户地址
	:param api_name:
	:param param:
	:return:
	'''
	print("业务需求: 查询地址list account_listAddress")
	address = api.request_Api(api_name, param)
	print(address)
	address_list = address["result"]
	print("当前系统中所有地址为:{},共有{}个".format(address_list, len(address_list)))
	return address_list


if __name__ == '__main__':
	api_name = "account_listAddress"
	param = []
	get_address_list()
