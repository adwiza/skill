import pprint
import csv

Indiana_Jones_stash = [['Name', 'year of discovery', 'quantity'],
                       ['Ark of the covenant', '1936', 1],
                       ['Crystal skull', '1957', 1]]
pprint.pprint(Indiana_Jones_stash)

indi_file = 'python_snippets/external_data/Indiana_stash.csv'

list_of_artefacts = []
inventory_of_stash = []

with open(indi_file, 'r') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        inventory_of_stash.append(row)

# with open(indi_file, 'r') as csv_file:
#     # csv_data = csv.reader(csv_file)
#     csv_data = csv.DictReader(csv_file, delimiter=',')
#     for row in csv_data:
#         name_of_item_from_the_stash = row['Name']
#         list_of_artefacts.append(name_of_item_from_the_stash)

print(f'Вся информация о таблице {inventory_of_stash[0]}')

# Запись в csv файл
# one_more_artifact_for_stash = {'Name': 'the Golden cross of Coronado', 'year of discovery': '1912', 'quantity': '1'}
# with open(indi_file, 'a', newline='') as out_csv:
#     csv_data_writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=inventory_of_stash[0])
#     csv_data_writer.writerow(one_more_artifact_for_stash)

print(csv.list_dialects())

with open('python_snippets/external_data/Indiana_stash.csv', 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(str(csvfile.readline()), [',', ';'])
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    print(dialect)  # <class 'csv.Sniffer.sniff.<locals>.dialect'>
    print(reader)  # <_csv.reader object at 0x018CFD30>


standard_need_list = []

with open('python_snippets/external_data/Tools for archaeological excavations.csv', 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        standard_need_list.append(row)

print(f'Стандартный набор инструментов {standard_need_list}')

indi_need_list = [{'Name:': 'Whip', 'Price:': '100', 'Quantity:': '1'},
                  {'Name:': 'Hat', 'Price:': '200', 'Quantity:': '2'},
                  {'Name:': 'Revolver', 'Price:': '400', 'Quantity:': '1'}]

with open('python_snippets/external_data/Tools for archaeological excavations.csv', 'w', newline='') as out_csv:
    writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=standard_need_list[0])
    writer.writeheader()
    writer.writerows(indi_need_list)

