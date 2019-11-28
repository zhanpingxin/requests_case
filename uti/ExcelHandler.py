
import xlrd
from settings import conf


class Excel_Handler(object):
    # @property

    def get_excel_data(self):


        book = xlrd.open_workbook(r'G:\testproject\MYTEST\requests_case\dome\接口测试示例.xlsx')

        sheet = book.sheets()[0]

        rows,cols = sheet.nrows,sheet.ncols

        l = []
        title = sheet.row_values(0)

        for i in range(1,rows):

            l.append(dict(zip(title,sheet.row_values(i))))
        return l

