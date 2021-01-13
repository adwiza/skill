import sqlite3
from pprint import pprint

conn = sqlite3.connect('python_snippets/external_data/Northwind.sl3')
# Укажем тип получаемых данных
conn.text_factory = bytes
# Создадим курсор - специальный объект, с помощью которого мы сможем делать запросы на SQL
cursor = conn.cursor()
#
# # Пример:
# # Требуется отобрать список заказов, для которых поле Freight (оплата за груз) больше значения 100,
# # а регион доставки (ShipRegion) -- 'RJ'
# cursor.execute('SELECT * FROM Orders WHERE (Freight > 100) AND (ShipRegion = "RJ")')
#
# # Получение отобранных значений:
# results = cursor.fetchall()
# results = '\n'.join(' | '.join(str(elem) for elem in r) for r in results)
# # print(f'Здесь выведется список значений, подходящие под заданные условия {results}')
# results_one_more_time = cursor.fetchall()
# # print(f'А здесь пустой список {results_one_more_time}')
# # Для повторного получения результов из курсора, необходимо создать новый запрос
# # cursor.execute('SELECT ContactName FROM Customers WHERE ContactName LIKE "% C%"')
# another_results = cursor.fetchall()
# another_results = '\n'.join(' | '.join(str(elem) for elem in r) for r in another_results)
# print(f'Список клиентов {another_results}')

# Удаление записи
# cursor.execute("DELETE FROM Orders WHERE OrderID='10'")
# conn.commit()

# Запись в БД:
# cursor.execute("INSERT INTO Orders (OrderID, CustomerID, EmployeeID) VALUES ('10', 'Anton', '5')")
# conn.commit()

cursor.execute('SELECT * FROM Orders WHERE OrderID = "10"')
changes = cursor.fetchall()
print(f'Внесенные нами изменения {changes}')

cursor.execute('UPDATE Orders SET EmployeeID=7 WHERE OrderID="10"')
conn.commit()

# Закрываем соединение
conn.close()







