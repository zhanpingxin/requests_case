'''
pip install xlrd
pip install xlwt

 excel操作的依赖包
'''


import xlrd



def get_excel_data():
    file_path = r'G:\testproject\MYTEST\requests_case\data\接口测试示例.xlsx'

    # 获取book列对象

    book = xlrd.open_workbook(file_path)
    #获取sheet对象

    sheet = book.sheets()[0]
    # 获取行和列
    rows,cols = sheet.nrows,sheet.ncols
    # print(rows,cols)

    # 定义空列表存储数据字典
    l = []
    #先获取第一行数据
    title = sheet.row_values(0)
    for i in range(1,rows):
        l.append(dict(zip(title,sheet.row_values(i))))
    return l

