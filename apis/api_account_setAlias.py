from apis.log import logger
from apis.API import request_Api


def account_setAlias(set_account, set_name):
	params = [set_account, set_name, "0x110", "0x30000"]  # api参数
	result = request_Api("account_setAlias", params)
	return result


if __name__ == '__main__':
	set_account = "0xad3dc2d8aedef155eaba42ab72c1fe480699336c"
	set_name = "doggs"
	account_setAlias(set_account, set_name)
