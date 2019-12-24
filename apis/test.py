#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: test.py
@time: 2019/12/24 12:09 下午
@desc:
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xlrd import open_workbook
from xlutils.copy import copy

r_xls = open_workbook("test.xls") # 读取excel文件
row = r_xls.sheets()[0].nrows # 获取已有的行数
excel = copy(r_xls) # 将xlrd的对象转化为xlwt的对象
table = excel.get_sheet(0) # 获取要操作的sheet

#对excel表追加一行内容
table.write(row, 0, '内容1') #括号内分别为行数、列数、内容
table.write(row, 1, '内容2')
table.write(row, 2, '内容3')

excel.save("test.xls") # 保存并覆盖文件