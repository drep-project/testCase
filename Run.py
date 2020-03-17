import _thread
from datetime import datetime
from time import sleep
import logging


def api(count, rootAccount, recivice):

	print("count: {}, {} --> {}".format(count,rootAccount, recivice))

# 1s 12
def times_of_120(account):
	count = 1
	while True:
		if count > 120:
			break
		logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易")
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易")
		api(count, "A-address", account)
		count = count + 1
		sleep(3)


# 单个账户发送 120 次交易
#times_of_120(account)


# 100个独立账户运行
def account_100_run_pay_120():
	for i in range(100):
		# 用户 xxx
		account = "Account---" + str(i)
		# 为一个用户创建一个线程 独立运行 120 次交易
		print("创建用户： " + account)
		times_of_120(account)
		#_thread.start_new_thread(times_of_120, (account,))

account_100_run_pay_120()