#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getBalance.py
@time: 2020/1/8 5:22 下午
@desc:
'''


'''
3. chain_getBalance
作用：查询地址余额
参数：

待查询地址
返回值：地址中的账号余额
示例代码
请求：
curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getBalance","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
响应：
{"jsonrpc":"2.0","id":3,"result":9987999999999984000000}
'''