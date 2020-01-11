#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: main.py.py
@time: 2020/1/1 11:33 上午
@desc:
'''
from logging import Logger
from script.creat_account import create_account_100

if __name__ == '__main__':
	# log = Logger(filename='Users/caroline/Desktop/Desktop/TestHome/block/logs/creat_account.log', level='debug')
	api_name = "account_createAccount"
	params = []
	create_account_100( peoples=1000000)
