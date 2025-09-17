from decimal import Decimal

num = Decimal('123.4567')
rounded_num = num.quantize(Decimal('1.00'))
print(rounded_num)