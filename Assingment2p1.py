phone_number = int(input())

Digit4 = phone_number%10000
phone_number //= 10000
Digit3 = phone_number%1000
AreaCode = phone_number // 1000

print('({}) {}-{}'.format(AreaCode, Digit3, Digit4))