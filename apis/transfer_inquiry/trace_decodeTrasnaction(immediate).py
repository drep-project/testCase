#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_decodeTrasnaction(immediate).py
@time: 2020/1/6 4:52 下午
@desc:
'''
from apis.API import request_Api
from apis.transfer_inquiry.trace_getRawTransaction import *


if __name__ == '__main__':
	api_name = "trace_getRawTransaction"
	# params = ["0x087adca1A1FCDCE8D21bcDe137e9ADCD66B282B0", 1, 10]
	params = ["0x83f569e149823631fcd5b11a12459d0c39a8abd5d24d20d5748b47977bbdaae8"]
	result = getRawTransaction(api_name, params)     #输入交易hash得到交易字节码
	result = result["result"] #通过字典拿到返回值中的交易字节码
	print("交易字节码{}".format(result))
	decodeTrasnaction(api_name="trace_decodeTrasnaction", params=[result])   #将得到的交易字节码解析成交易详情，传入的交易字节码需手动强转为数组
	