#Conditional lessons
#Boolean Expressions

# 3 == 3
# 3 == 2

# x = 5
# y=6

# print(x < y)

#more complex expressions
var_3,var_4,var_5 = 15, 20, 25

print('var_3 =', var_3, 'var_4 =', var_4, 'var_5 =', var_5, end = '\n\n')
print('var_4 and var_5 < 100?', var_4 < 100 and var_5 < 100)
print('var_4 and var_5 < 22?', var_4 < 22 and var_5 < 22)
print('var_4 or var_5 < 22?', var_4 < 22 or var_5 < 22, end = '\n\n')

# NOT True = False
# NOT False = True
print('not True is:',not True)
print('not false is:',not False)

#if statements

# some_condition = False

# if some_condition is:
#     print('The variable \'some_condition\' is True')
# else:
#     print('The variable \'some_condition\' is False')

temp = int(input('Please enter the temperature in Celsius. \ An integer between 0-40:>>>>'))

if temp > 30:
    print('Wear shorts and sun screen!')
elif temp <= 30 and temp > 20:
    print('It\'s warm, but not shorts weather!')
elif temp <= 20 and temp > 10:
    print('You\'ll probably need a vest today!')
else:
    print('Too Cold! don\'t go out!')


