import requests
import json
import threading


class myThread(threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
	
	def run(self):
		print("开始线程：" + str(self.threadID))
		creat_account()
		print("退出线程：" + str(self.threadID))


# 创建账户
def creat_account():
	url = "http://127.0.0.1:15645"
	
	payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_createAccount\",\n\t\"params\":[], \n\t\"id\": 3\n\t\n}"
	headers = {
		'Content-Type': "application/json",
		'cache-control': "no-cache",
		'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
	}
	try:
		response = requests.request("POST", url, data=payload, headers=headers)
		print("creat_account_response:{}", response.text)
		jsonDic = json.loads(response.text)
		return jsonDic['result']
	except:
		print("HTTP error")
		response = requests.request("POST", url, data=payload, headers=headers)
		print("creat_account_response:{}", response.text)
		return "error Account"


def account_100_run_pay_120(peoples=1000000):
	account_100 = []
	for i in range(peoples):
		# 用户 xxx
		try:
			account = creat_account()
			print("创建用户： {}".format(i) + account)
			account_100.append(account)
			threadX = myThread(i, )
			threadX.start()
		except Exception as e:
			print("账户创建失败!")


account_100_run_pay_120(1000000)
