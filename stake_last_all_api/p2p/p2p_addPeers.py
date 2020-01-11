#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: p2p_addPeers.py
@time: 2020/1/8 5:32 下午
@desc:
'''

from stake_last_all_api.API import request_Api

''' p2p_addPeers
'''


def addPeers(api_name, params):
	'''
	添加节点
	:param api_name: p2p_addPeers
	:param params: 添加的节点的p2p信息+ip地址,以数组的形式传入
	:return: nil
	示例代码
	"enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:55555"
	'''
	try:
		result = request_Api(api_name, params)
		print("添加节点，返回值为{}".format(result))
		return result
	except Exception as e:
		print("添加节点返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "p2p_addPeers"
	params = ["enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:44444"]
	addPeers(api_name, params)
