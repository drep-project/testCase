#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getAliasByAddress.py
@time: 2020/1/8 5:24 下午
@desc:
'''



''''

7. chain_getAliasByAddress
作用：根据地址获取地址对应的别名
参数：

待查询地址
返回值：地址别名
示例代码
请求：
curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAliasByAddress","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
响应：
{"jsonrpc":"2.0","id":3,"result":"tom"}

'''