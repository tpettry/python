# Question 1 
# Write code that asks the user to input a number between 1 and 5 inclusive.  
# The code will take the integer value and print out the string value.
# So for example if the user inputs 2 the code will print two. 
# Reject any input that is not a number in that range.

user_input = int(input('Please enter in a number between 1-5 \n >>>>'))

if user_input == 1:
    print('one')
elif user_input == 2:
    print('two')
elif user_input == 3:
    print('three')
elif user_input == 4:
    print('four')
elif user_input == 5:
    print('five')
else:
    print(user_input, 'Is not a specified number requested')


# Question 2
# Repeat the previous task but this time the user will input a string
# and the code will output the integer value Convert the string to lowercase first.

user_input = input('Please enter in a string number between One-Five \n >>>>')

user_input = user_input.lower()

if user_input == 'one':
    print(1)
elif user_input == 'two':
    print(2)
elif user_input == 'three':
    print(3)
elif user_input == 'four':
    print(4)
elif user_input == 'five':
    print(5)
else:
    print(user_input, 'Is not a specified string number requested')

# Question 3
# Create a variable containing an integer between 1 and 10 inclusive.
# Ask the user to guess the number.
# If they guess too high or too low, tell them they have not won.
# Tell them they win if they guess the correct number.

user_input = input('Guess the number I am thinking off between 1 and 10 \n >>>>')

secret_num = 3

if user_input.isdigit():
    user_input = int(user_input)
    if user_input < secret_num:
        print('you guess too low')
    elif user_input > secret_num:
        print('Guess is too high')
    elif user_input == secret_num:
        print('congrats you guess the number')
    else:
        print('you didn\'t even try')
else:
    print('What game are you playing?')


#Question 4
#