import win32com.client

class easyExcel:
    """A utility to make it easier to get at Excel. Remebering to
    save the data is your problem, as is error handling.
    Operates on one workbook at a time."""

    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        #xl = win32.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ""

    def sace(self, newfilename=None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()

    def close(self):
        self.xlBook.Close(SaveChanges=1)#是否存储文件   1保存 0取消
        del self.xlApp

    def getCell(self, sheet, row, col):
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).value

    def set(self, sheet, row, col, value):
        "Set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value


if __name__ == "__main__":
    ii = easyExcel()
    ii.sace('D:\\ssd')
    ii.set(1,2,2,33333)
    print(ii.getCell(1,1,1))
    ii.close()
