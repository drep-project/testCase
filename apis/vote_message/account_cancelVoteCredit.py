#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_cancelVoteCredit.py
@time: 2020/1/8 12:09 下午
@desc:
'''

from apis.API import request_Api


def cancelVoteCredit(api_name, params):
	'''
	#撤销投票
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_cancelVoteCredit","params":["0x300fc5a14e578be28c64627c0e7e321771c58cd4","0x0ad472fd967eb77fb6e36ec40901790065155d5e","0xf4240","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
	:param api_name:account_cancelVoteCredit
	:param params: fromd地址，to地址，金额，gas价格，手续费
	:return:交易hash
	'''
	result = request_Api(api_name, params)
	print("撤销投票结果返回为{}".format(result))


if __name__ == '__main__':
	api_name = "account_cancelVoteCredit"
	params = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0", "2", "0xf4240", "0x110", "0x30000"]
	cancelVoteCredit(api_name, params)
