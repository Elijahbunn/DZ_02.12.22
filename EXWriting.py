import pandas as pd
import xlrd, xlwt
import openpyxl

def Excel_file_writing(list1):
    list_txt = ['name: ', 'surname: ', 'race: ', 'age: ', 'growth: ',
                'clothes: ', 'facialfeatures: ', 'appearancefeatures: ',
                'strength: ', 'intelligence: ', 'skills: ', 'speed: ',
                'agikity: ', 'magic: ']
    book = xlwt.Workbook(encoding="utf-8") 
    sheet1 = book.add_sheet("Python Sheet 1")
    for i in range(len(list_txt)):
        sheet1.write(0, i, str(*[list_txt[i]]))
        sheet1.write(1, i, str(*[list1[i]]))
    book.save("Persona.xls")
