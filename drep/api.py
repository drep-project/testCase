#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests

name = ""
paramsa = []


def all_Api(name, paramsa):
	url = "http://127.0.0.1:15645"
	
	payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"chain_getBalance\",\n\t\"params\":[\"0xad3dc2d8aedef155eaba42ab72c1fe480699336c\"],\n\t\"id\": 3\n\t\n}\n"
	# print(payload)
	jsonDic = json.loads(payload)  # 转换为python格式
	# print(jsonDic)
	jsonDic["method"] = name
	jsonDic["params"] = paramsa
	# print(payload)
	payload = json.dumps(jsonDic)  # 转化为json格式
	# print(payload)
	print("api名字: {}  -- 参数: {}".format(name, paramsa))
	
	headers = {
		
		'Content-Type': "application/json",
		'cache-control': "no-cache",
		'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
	}
	
	try:
		response = requests.request("POST", url, data=payload, headers=headers)
		# print("getBalance:", response.text)
		jsonDic = json.loads(response.text)
		return jsonDic,jsonDic['result']
	except:
		print("api error")
		return "error api"


if __name__ == '__main__':
	# name = "chain_getBalance"
	# paramsa = ["0x8a8e541ddd1272d53729164c70197221a3c27486"]
	
	a = all_Api(name="account_createAccount", paramsa=[])
	print(a)
