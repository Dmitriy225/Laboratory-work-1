import openpyxl
#import openpyxl.styles
from openpyxl.styles import Font, Color

def create_xlsx(books):
    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)
    sheet_1 = workbook.create_sheet("Книги")
    sheet_1.column_dimensions['A'].width = 100
    sheet_1.column_dimensions['B'].width = 50
    sheet_1.append(["Название книги", "Автор", "Цена"])
    titleFont = Font(sz=14, bold=True)
    sheet_1['A1'].font = titleFont
    sheet_1['B1'].font = titleFont
    sheet_1['C1'].font = titleFont
    for book in books:
        sheet_1.append([book.name, book.author, book.price])
    workbook.save("test.xlsx")