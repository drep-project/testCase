#coding=utf-8
import xlwt
import xlrd

# def save_balance_accou ():
#     try:
#         # 创建excel文件
#         filename=xlwt.Workbook()
#         # 给工作表命名，test
#         sheet=filename.add_sheet("test")
#         # 写入内容，第4行第3列写入‘张三丰’
#         hello=u'张三丰'
#         sheet.write(3,2,hello)
#         # 指定存储路径，如果当前路径存在同名文件，会覆盖掉同名文件
#         filename.save("test1.xls")
#     except Exception as e:
#         print(str(e))
#     #     找到读取文件
#     filename='test1.xls'
#     # 打开excel文件
#     date=xlrd.open_workbook(filename)
#     # 根据工作表名称，找到指定工作表  by_index(0)找到第N个工作表
#     sheet=date.sheet_by_name('test')
#     # 读取第四行第三列内容，cell_value读取单元格内容,指定编码
#     value=sheet.cell_value(3,2).encode('utf-8')
#     print(value)
# def save_balance_accou (result):
# 	f = xlwt.Workbook()  # 创建工作簿
# 	sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
# 	for i in range(len(l_)):
# 		sheet1.write(0, i, i)  # 表格的第一行开始写。第一列，第二列。。。。
# 	# sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
# 	f.save('text.xls')  # 保存文件
