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

# temp = int(input('Please enter the temperature in Celsius. \ An integer between 0-40:>>>>'))

# if temp > 30:
#     print('Wear shorts and sun screen!')
# elif temp <= 30 and temp > 20:
#     print('It\'s warm, but not shorts weather!')
# elif temp <= 20 and temp > 10:
#     print('You\'ll probably need a vest today!')
# else:
#     print('Too Cold! don\'t go out!')

#more things that can be done with strings
my_string = 'Python'

#length of characters 
print(len(my_string))
#give me first position
#my_string[0]
#give me second position
#my_string[1]
#give me first 4 characters
#my_string[0:4]
#a different way to get first 4 characters
#my_string[:4]
#give me the last character
#my_string[-1]
#assign variable to a position of a string 
#letter = my_string[4]
#convert string to uppercase and lowercase
# my_string.upper()
# my_string.lower()

#game example

word = 'summer'

guess = input('I\'m thinking of a word, can you guess the word? Hint \
    it\'s a season.>>>')

guess = guess.lower()

if guess == 'summer':
    print('Yes you got it right')
elif guess == 'winter':
    print('No you are wrong')
elif guess == 'fall':
    print('you thought you could guess the answer lol')
elif guess == 'spring':
    print('you wish it was spring time')
else:
    print('not even close')

