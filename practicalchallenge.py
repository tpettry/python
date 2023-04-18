#Question 1 Ask the user for two numbers between 1 and 100. Then count from the lower number to the higher number. Print the results to the screen.

# num_1 = int(input('Please enter a number between 1 and 100 :> '))
# num_2 = int(input('Please enter a second number that is between 1 and 100 :>'))

# while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print('Numbers must be different values between 1 and 100 try again')
#     num_1 = int(input('Please enter a number between 1 and 100'))
#     num_2 = int(input('Please enter a number between 1 and 100'))
    
# if num_1 < num_2:
#     for i in range(num_1, num_2+1):
#         print(i, end=' ')
# else:
#     for i in range(num_2, num_1+1):
#         print(i, end=' ')


#Question 2 Ask the user to input a string and the print it out to the screen in reverse order(use a for loop).

# word = input('Please enter in your favorite color')
# reverseword = ' '
# for char in word:
#     reverseword = char + reverseword

# print(reverseword, end= ' ')
# #another way you can do this
# print(word[::-1])

# #Question 3 Ask the user for a number between 1 and 12 and then display a times table for that number

# user_input = input('Please enter a number between 1 and 12 :> ')

# while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) > 12):
#     print('must enter a number between 1 and 12')
#     user_input = input('Please enter a number betwen 1 and 12 and stop being stupid')
# user_input = int(user_input)
# print('=============================')
# print()
# print(f'This is the {user_input} times table')
# print()
# for i in range(1,13):
#     print(f'{i} x {user_input} = {i*user_input}')
    
# #Question 4 Can you amend the solution to question 3 so that it just prints out a times tables between 1 and 12? (no need to ask user for input)

# for i in range(1, 13):
#     print('=================')
#     print()
#     print(f'This is the {i} times table')
#     print()
#     for num in range(1,13):
#         print(f'{i} x {num} = {i*num}')

#Question 5 Ask the user to input a sequence of numbers. Then Calculate the mean and print the result.

# user_input = input('Please enter a number type exit to stop')
# numbers = []
# while user_input.lower() != 'exit':
#     while not user_input.isdigit():
#         print('That is not a number! Numbers Only please:> ')
#         user_input = input('Try again:>')
#     numbers.append(int(user_input))
#     user_input = input('Please enter next number')
# total = 0 
# for number in numbers:
#     total += number
    
# print(f'Mean is {total/len(numbers)}')
# print(sum(numbers)/len(numbers))

#Question 6 Write code that will calculate 15 factorial.  (factorial is product of positive ints up to a given number e.g 5 factorial is 5x4x3x2x1)

# user_input = int(input('Please enter in a number'))
# n = user_input
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# #Question 7 
# #Write code that calculate Fibonacci numbers. Create list containing forst 20 Fibonacci numbers made by sum of preceeding two. Series starts 0 1 1 2 3 5 8 13 19....)

# ##number of fib numbers required
# user_num = int(input('Please enter desire Fibonaccia sequence number:>'))
# n = user_num

# #Set a and b to the first two numbers in the sequence
# a = 0 
# b = 1

# #List in which to store numbers
# fib_nums = []

# #Use a for loop to create the sequence, repeat n times
# for i in range(n):
#     fib_nums.append(a)
#     a,b = b,a+b

# print(f'The first {n} Fibonacci numbers are, {fib_nums}')

#Question 10 Write some code that will determine all odd and even numbers between 1 and 100. Put the odds in list called odd and even in a list called even.

#Numbers required
userinput = int(input('Please enter in a number for system to guess odds and even'))
n = userinput

#Instantiate empty lists
evens = []
odds = []

for i in range(n+1):
    if not i % 2: 
        evens.append(i)
    else: 
        odds.append(i)
print(f'The evens are {evens}')
print(f'The odds are {odds}')
