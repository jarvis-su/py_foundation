import openpyxl

excel_file_name = '../materials/example.xlsx'
wb = openpyxl.load_workbook(excel_file_name)
file_type = type(wb)

sheet_names = wb.sheetnames
for name in sheet_names:
    sheet = wb.get_sheet_by_name(name)



print('end')