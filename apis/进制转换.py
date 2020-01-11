#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: 进制转换.py
@time: 2019/12/25 11:49 上午
@desc:
'''
def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""

    if num < 0:
        num = num + 2 ** 32

    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr

    return hexStr

if __name__ == '__main__':
    result = toHex(1000000)
    print(result)