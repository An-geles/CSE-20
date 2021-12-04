user_num = int(input())
x = int(input())

# Main Part of Code
a = user_num//x
b = a//x
c = b//x

print(a, b, c)

# Expression for Calories burned during workout

# Input for variables A,W,H,T
Age = int(input())
Weight = int(input())
Heart_Rate = int(input())
Time = int(input())

# Equations for calories burnt in Women and Men
calories_women = (((Age * 0.074) - (Weight * 0.05741) + (Heart_Rate * 0.4472) - 20.4022) * Time / 4.184)
calories_man = (((Age * 0.2017) + (Weight * 0.09036) + (Heart_Rate * 0.6309) - 55.0969) * Time / 4.184)

Men = calories_man
Women = calories_women

print(' women: {:.2f} calories'.format(calories_women))
print(' Men: {:.2f} calories'.format(calories_man))


