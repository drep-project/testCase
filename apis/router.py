from apis.api_chain_getBalance import chain_getBalance, getBalance_of_all_address_list
from apis.api_chain_transaction import transaction_one, random_transaction
from apis.api_create_account import create_account, create_account_100
from apis.api_get_addresslist import get_address_list
from apis.time_of_account_1 import transation_120_account_1

api_route = {
	"create_account": create_account,
	"create_account_100": create_account_100,
	"get_address_list": get_address_list,
	"transaction_one": transaction_one,
	"random_transaction": random_transaction,
	"chain_getBalance": chain_getBalance,
	"getBalance_of_all_address_list": getBalance_of_all_address_list,
	# "creat_one_wallet_account": creat_one_wallet_account,
	"transation_120_account_1": transation_120_account_1,
	
}


# API 总函数
def runCase(case_name):
	"""
	
	:param case_name:
	:return: 注意格式   xxx(case_name)()
	"""
	return api_route.get(case_name)()


if __name__ == '__main__':
	print(runCase("create_account_100"))
	print(runCase("create_account"))
