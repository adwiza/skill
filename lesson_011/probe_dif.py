stroka = '48375'

first_digit = int(stroka[:1])
second_digit = int(stroka[1:2])
third_digit = int(stroka[-1:])
four_digit = int(stroka[-2:-1])
print(first_digit, second_digit, '*****', third_digit, four_digit)
left = first_digit + second_digit
right = third_digit + four_digit

if left == right:
    print(f'Число счастливое {left} = {right}', stroka)
else:
    print(f'Число обычное {left} = {right}', stroka)
