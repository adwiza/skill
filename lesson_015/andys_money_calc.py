from decimal import Decimal, getcontext

Andys_money_float = []
Andys_money_decimal = []

with open('python_snippets/external_data/Randalls_money.txt', 'r') as Randalls_money:
    for line in Randalls_money:
        Andys_money_float.append(float(line))
        Andys_money_decimal.append(Decimal(line))

exchange_rate_roubles_in_dollars = 1.2063  # Курс 1972 года
profit_tax_rate = 0.13


def tax_calculation(income_in_dollars, exchange_rate, tax_rate):
    return tax_rate * exchange_rate * sum(income_in_dollars)


# Проблема №1 - Недостаточная точность при сведении баланса при подсчете налогов:

profit_tax_amount = tax_calculation(Andys_money_float, exchange_rate_roubles_in_dollars, profit_tax_rate)
print(f'Итоговая сумма налога {profit_tax_amount}')

d_profit_tax_amount = tax_calculation(Andys_money_decimal, Decimal(exchange_rate_roubles_in_dollars),
                                      Decimal(profit_tax_rate))
print(f'Итоговая сумма налога {d_profit_tax_amount}')

# Зачастую разница незаметна, но она есть
print(f'Разница в одном таком расчете: {d_profit_tax_amount - Decimal(profit_tax_amount)}')

print()
# Итог №1
# Даже при относительно простых операцияхс относительно небольшим количеством товаров,
# появляется и копится разница в расчетах.
# Decimal позволяет контролировать точность расчетов.

# Проблема №2 - Ценообразование и округление:

Andys_price_list_float = []
Andys_price_list_decimal = []

with open('python_snippets/external_data/Andys_goods.txt', 'r') as Andys_goods:
    for price in Andys_goods:
        Andys_price_list_float.append(float(price))
        Andys_price_list_decimal.append(Decimal(price))

print(f'Цены в магазинах не могут выглядеть так {Andys_money_float[:5]}')

rounded_list_for_pricing = []
for price in Andys_price_list_float:
    rounded_list_for_pricing.append(price.__round__(2))
revenue_for_the_day = sum(rounded_list_for_pricing)
print(f'Но даже если цены выглядят ровно {rounded_list_for_pricing[:5]}')
print(f'Могут возникать странные остатки при их суммированиии {revenue_for_the_day}')

decimal_rounded_list_for_pricing = []
for price in Andys_price_list_decimal:
    decimal_rounded_list_for_pricing.append(price.quantize(Decimal('1.00')))
decimal_revenue_for_the_day = sum(decimal_rounded_list_for_pricing)
print(f'Получаем округлёенные цены {decimal_rounded_list_for_pricing[:5]}')
print(f'Считаем дневную выручку {decimal_revenue_for_the_day}')
print(f'Равны ли значения. Ответ - {revenue_for_the_day == decimal_revenue_for_the_day}')
print()


def muller_formula(z, y):
    return 108 - (815 - 1500 / z) / y


# Сперва с помощью 'float'
float0 = 4.0
float1 = 4.25

for _ in range(2, 31):
    float2 = muller_formula(float0, float1)
    float0, float1 = float1, float2

print(f'(float) 30 член последовательности равен {float2}')

# А теперь попробуем использовать Decimal

getcontext().prec = 35
dec0 = Decimal(4.0)
dec1 = Decimal(4.25)
for _ in range(2, 31):
    dec2 = muller_formula(dec0, dec1)
    dec0, dec1 = dec1, dec2

print(f'(Decimal) 30 член последовательности равен {dec2}')

# Разница не так уж велика, но что будет, если увеличить точность вычислений до 50

getcontext().prec = 50
dec0_50 = Decimal(4.0)
dec1_50 = Decimal(4.25)
for _ in range(2, 31):
    dec2_50 = muller_formula(dec0_50, dec1_50)
    dec0_50, dec1_50 = dec1_50, dec2_50

print(f'Теперь 30 член последовательности равен {dec2_50}')
print(f'Разница между первым и вторымвычисленным составила {dec2 - dec2_50}')
