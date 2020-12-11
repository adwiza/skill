# Сериализация (запись):
import json

data = {
   "FirstName": "Dominick",
   "LastName": "Cobb",
   "Adress": {
       "city": "Los Angeles",
       "StreetAdress": "S Olive st 617",
   },
   "ContactDetails": {
       "PhoneNumbers": ["+1 212-626-8118", "+1 212-484-4554"],
       "E-mail": "inception@nolan.genii",
   }
}

# Запись в файл

with open('python_snippets/external_data/Dom_3.json', 'w') as write_file:
    json.dump(data, write_file)

# Запись в переменную

json_data = json.dumps(data)
print(f'Словарь будет преобразован в формат JSON в виде строки {json_data}')

# Данный меторд имеет несколько интересных параметров

json_data_with_indent = json.dumps(data, indent=4)
print(f'Та же строка, но уже с отступами в удобном виде {json_data_with_indent}')

with open('python_snippets/external_data/Dom_4.json', 'w') as write_file:
    write_file.write(json_data_with_indent)

json_data_with_indent = json.dumps(data, indent=4, sort_keys=True)
print(f'В результатетключи будут отсортированы {json_data_with_indent}')

with open('python_snippets/external_data/Dom_4.json', 'r') as read_file:
    loaded_json_file = json.load(read_file)

print(f'В итоге строка, которую мы загрузили в файл Dom_4 превратилась обратно в словарь {loaded_json_file}')
print(f'И мы можем получить доступ {loaded_json_file["FirstName"]}')
print(f'Или более к сложному полю: {loaded_json_file["Adress"]["city"]}')

# Чтение из переменной

loaded_json_str = json.loads(json_data)

print(f'Строка превращается обратно в словарь: {loaded_json_str}')  # class dict

print('*' * 100)

# Practice

with open('python_snippets/external_data/json_todos.json', 'r') as json_file:
    list_of_tasks = json.load(json_file)

number_of_tasks = len(list_of_tasks)
print(f'Пример записи {list_of_tasks[0]}')

unique_users = set()
for number in range(number_of_tasks):
    unique_users.add(list_of_tasks[number]['userId'])
print(f'Количество уникальных пользователей {len(unique_users)}')

users = {}
for task in range(number_of_tasks):
    users[list_of_tasks[task]['userId']] = {'num': 0, 'completed': 0}

for task_number in range(number_of_tasks):
    users[list_of_tasks[task_number]['userId']]['num'] += 1
    if list_of_tasks[task_number]['completed'] is True:
        users[list_of_tasks[task_number]['userId']]['completed'] += 1

print(f'У пользователя под номером 1 всего {users[1]["num"]} задач, из них {users[1]["completed"]} уже выполнено')

with open('python_snippets/json_todos_formated.json', 'w') as json_file:
    json.dump(users, json_file, indent=4)