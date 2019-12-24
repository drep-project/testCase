#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: Utils.py
@time: 2019/12/23 10:56 下午
@desc:
'''

import xlrd
import xlwt


def get_real_value(value):
    """
    获取真实值，由于xlrd读取excel的整数时使用float表示，导致整数带有小数点，所以这里需要做处理
    :param value:
    :return:
    """
    if type(value) is float:
        if value % 1 == 0:
            return int(value)
    return value


def excel_read(path, sheet_index=0):
    """
    读取Excel文件
    :param path: 文件路径，包含文件名称
    :param sheet_index: Excel表单索引
    """
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(sheet_index)
    rows = sheet.nrows
    data = []
    for r in range(rows):
        data.append(list(map(get_real_value, sheet.row_values(r))))
    return data


def excel_read_dict(path, sheet_index=0):
    """
    读取Excel文件\n
    :param path: 文件路径，包含文件名称
    :param sheet_index: Excel表单索引
    """
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(sheet_index)
    header = sheet.row_values(0)
    rows = []
    for r in range(1, sheet.nrows):
        row_values = sheet.row_values(r)
        row_dict = {}
        for c in range(sheet.ncols):
            cell_value = get_real_value(row_values[c])
            row_dict[header[c]] = cell_value
        rows.append(row_dict)
    return rows


def excel_write(path, rows):
    """
    将数据写入Excel文件\n
    :param path: 文件路径，包含文件名称
    :param rows: 二维数组数据列表
    """
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建表
    worksheet = workbook.add_sheet('sheet 0')
    # 写数据
    for row_index in range(len(rows)):
        row = rows[row_index]
        for col_index in range(len(row)):
            cell = row[col_index]
            worksheet.write(row_index, col_index, label=cell)
    # 保存
    workbook.save(path)
   
 
    
if __name__ == '__main__':
    
    excel_write('test.xls', [['编号', '姓名', '年龄'], ['1', '小明', 10], ['2', '花花', 8]])
    excel_write('./before_price.xls', [['发送者', '接收者', '交易金额', '发送者交易前余额', '接收者交易前余额'],
                                       ["sendAccount", "receiveAccount", "price",
                                        "send_account_balance_before",
                                        "receive_account_balance_before"]])
    print(excel_read_dict('test.xls'))
   