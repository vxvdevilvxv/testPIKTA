"""
Предположение о распределении значений в таблице сделано исходя из логического совпадения названия столбца
и входных данных
"""

import openpyxl
import json
import os
import re

sheet_index = 1
book = openpyxl.Workbook()
sheet = book.active

for file_name in os.listdir():
    if file_name.endswith('.json'):

        with open(file_name, 'r', encoding='utf-8') as file:
            content = json.load(file)

        headers_dict = {content['headers'][i]['properties']['QuickInfo']: 0 for i in range(len(content['headers']))}
        sheet.append(list(headers_dict.keys()))

        for j in range(len(content['values'])):
            current_value = content['values'][j]['properties']['Text']

            if re.match(r' ?\d \d+,\d\d', current_value):
                headers_dict['Сумма во ВВ'] = current_value

            elif re.match(r'[A-Z]{3}', current_value):
                headers_dict['Внутренняя валюта'] = current_value

            elif re.match(r'[A-Z]{2}', current_value):
                headers_dict['Код налога'] = current_value

            elif re.match(r'[0-9]{2}-[0-9]{6}', current_value):
                headers_dict['Счет Главной книги'] = current_value
            if (j + 1) % 4 == 0:
                sheet.append(list(headers_dict.values()))

        book.create_sheet()
        sheet = book[f'Sheet{sheet_index}']
        sheet_index += 1

book.remove(sheet)
book.save('book.xlsx')
book.close()
