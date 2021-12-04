# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pets_name = input("Enter pet's name:\n")
number_choice = input("Enter a number:\n")
print('You entered:',favorite_color, pets_name, number_choice)


# FIXME (2): Output two password options
password1 = favorite_color + '_' + pets_name
password2 = number_choice + favorite_color + number_choice
print('\nFirst password:',password1)
print('Second password:',password2)

# FIXME (3): Output the length of the two password options
password1_length = len(password1)
password2_length = len(password2)
print("\nNumber of characters in",password1+':',password1_length)
print("Number of characters in",password2+":",password2_length)