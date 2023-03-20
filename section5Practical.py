# Question 1 
# Write code that asks the user to input a number between 1 and 5 inclusive.  
# The code will take the integer value and print out the string value.
# So for example if the user inputs 2 the code will print two. 
# Reject any input that is not a number in that range.

# user_input = int(input('Please enter in a number between 1-5 \n >>>>'))

# if user_input == 1:
#     print('one')
# elif user_input == 2:
#     print('two')
# elif user_input == 3:
#     print('three')
# elif user_input == 4:
#     print('four')
# elif user_input == 5:
#     print('five')
# else:
#     print(user_input, 'Is not a specified number requested')


# Question 2
# Repeat the previous task but this time the user will input a string
# and the code will output the integer value Convert the string to lowercase first.

# user_input = input('Please enter in a string number between One-Five \n >>>>')

# user_input = user_input.lower()

# if user_input == 'one':
#     print(1)
# elif user_input == 'two':
#     print(2)
# elif user_input == 'three':
#     print(3)
# elif user_input == 'four':
#     print(4)
# elif user_input == 'five':
#     print(5)
# else:
#     print(user_input, 'Is not a specified string number requested')

# Question 3
# Create a variable containing an integer between 1 and 10 inclusive.
# Ask the user to guess the number.
# If they guess too high or too low, tell them they have not won.
# Tell them they win if they guess the correct number.

# user_input = input('Guess the number I am thinking off between 1 and 10 \n >>>>')

# secret_num = 3

# if user_input.isdigit():
#     user_input = int(user_input)
#     if user_input < secret_num:
#         print('you guess too low')
#     elif user_input > secret_num:
#         print('Guess is too high')
#     elif user_input == secret_num:
#         print('congrats you guess the number')
#     else:
#         print('you didn\'t even try')
# else:
#     print('What game are you playing?')


#Question 4
#Ask the user to input their name. Check the length of the name. If it is 
#greater than 5 characters long, write a message telling them how many characters
#otherwise write a message saying the length of their name is a secret.

# user_input = input('Please enter your name >>>>')

# length_input = len(user_input)

# if length_input <= 5:
#     print('the length of your name is a secret')
# elif length_input > 5:
#     print(length_input)
# else :
#     print('I don\'t know what is going on.')
    
# Question 5
#Ask the user for two integers between 1 and 20.  If they are both greater than 
#15 return their product. If only one is greater than 15 return their sum, if
#neither are greater than 15 return zero

# user_input1 = int(input('Please enter a number between 1 and 20 >>>>'))
# user_input2 = int(input('Please a second number between 1 and 20 >>>>'))

# if user_input1 > 15 and user_input2 > 15:
#     print(user_input1*user_input2)
# elif user_input1 > 15 or user_input2 > 15:
#     print(user_input1 + user_input2)
# else:
#     print(0)
    
#Question 6
#Ask the user for two integers, then swap the contents of the variables.  So if
#var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2 
#and var_2 should equal 1

var_1 = input('Please enter in an integer >>>')
var_2 = input('Please enter in a second integer >>>')

print('var_1 =',var_1, 'var_2 = ',var_2)
var_1,var_2 = var_2,var_1
print('var_1 =',var_1, 'var_2 = ',var_2)
