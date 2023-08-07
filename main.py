import openpyxl

filepath = "test_01.xlsx"
book = openpyxl.Workbook()
book.save(filepath)
