'''
Задание 2: Процесс «Проверка актуальных платежных реквизитов на сайте ИФНС»
'''

import json
import requests

url = 'https://service.nalog.ru/addrno-proc.json'

param_dict = {
    "c": "next",
    "step": "1",
    "npKind": "fl",
    "objectAddr": "",
    "objectAddr_zip": "",
    "objectAddr_ifns": "",
    "objectAddr_okatom": "",
    "ifns": "7840",
    "oktmmf": "40913000",
    "PreventChromeAutocomplete": ""
}
response = requests.post(url, data=param_dict).json()

with open('payment_details.json', 'w', encoding='utf-8') as file:
    json.dump(response['payeeDetails'], file, ensure_ascii=False, indent=4)
