# testPIKTA

список зависимостей расположен в requirements.txt

task1.py
Условие задачи:
Вам дано 3 файла json. Каждый файл представляет из себя структуру: {“headers”: [], “values”: []}
Необходимо распарсить все json и записать данные в один файл excel в виде таблицы, где заголовки – headers, а значения – values (каждый файл на отдельном листе excel).

У каждого элемента из headers необходимо в качестве значения использовать свойство QuickInfo, а у элементов values в качестве значения использовать свойство Text.

Порядок следования элементов внутри headers может не всегда соответствовать порядку внутри values.
Для одного json порядок следования элементов внутри headers может не всегда соответствовать порядку внутри headers другого файла (аналогично и для values).

На выходе должен получиться один файл excel c 3 листами, на каждом листе должна быть таблица

Результат:
файл book.xlsx

task2.py

Условие задачи:
Необходимо написать функцию с REST запросом, которая будет получать платежные реквизиты по введенным аргументам.
Входные данные: Код ИФНС (7840), ОКТМО (40913000)
Выходные данные: Массив с набором данных (Получатель платежа, ИНН получателя, КПП получателя, Банк получателя, БИК, Счет №)

Результат:
файл payment_details.json


task3.txt

Условие задачи:
Необходимо написать три запроса:
1)	Список клиентов с общей суммой их покупок
2)	Список клиентов, которые купили телефон
3)	Список товаров с количеством их заказов

Результат:
task3.txt