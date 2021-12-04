# Initial prompt
user_num = int(input('Enter integer:\n'))
print('You entered:', user_num)

# Arithmetic for first problem set
# Separate problems with subscripts x/y1 and x/y2
x1 = user_num * user_num
y1 = x1 * user_num
print(user_num, 'squared is', x1,)
print('And', user_num, 'cubed is', y1, '!!')

# Arithmetic for second problem set
user_num2 = int(input('Enter another integer:\n'))
x2 = 4 + user_num2
y2 = 4 * user_num2
print('4 +', user_num2, 'is', x2)
print('4 *', user_num2, 'is', y2)
