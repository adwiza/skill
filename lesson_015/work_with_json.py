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
