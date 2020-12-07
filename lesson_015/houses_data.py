import csv

street_of_houses = set()

with open('python_snippets/external_data/houses.csv', 'r') as csv_file:
    csv_data = csv.DictReader(csv_file, delimiter=',')
    for row in csv_data:
        house_street = row['Street']
        street_of_houses.add(house_street)

print(f'В итоге мы получили список улиц всех домов из таблицы {street_of_houses}')
