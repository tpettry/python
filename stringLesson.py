#String lesson

#phrase_1 = 'The cat sat on the mat!'
#phrase_2 = 'And so did the dog!'
#phrase_3 = phrase_1 + ' ' + phrase_2

#print(phrase_3)


#user_input = int(input('How many apples do you have? >>>'))
#type(user_input) will give us what type is the variable int or str
#print(user_input)

#question 1
# Ask the user for the radius of a circle and then print the area

radius = float(input('Please enter the radius:>>>>'))
pi = 3.14159
area = pi * radius**2
print('You have enter' , radius, 'the area of the circle is', area)

#question 2
# Convert fahrenheit to celsius
far = float(input('Please enter the temperature in Fahrenheit:>>>>'))
cel = (far - 32) * 5/9
print('Fahrenheit temperature was:', far, 'Convert Celsius is:', cel)

#question 3
# Obtain the sum of two integers

num_1 = int(input('Please enter first number:'))
num_2 = int(input('Please enter second number:'))
sum_num = num_1 + num_2

print('Total of two numbers are:', sum_num)

#question 4 
#product of two integers

num_3 = int(input('Please enter a number:'))
num_4 = int(input('Please enter a second number:'))
prod_num = num_3 * num_4

print('The Product of these two numbers is:', prod_num)

#question 5 
# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza.  The local pizza shop sells pizzas of only 6 slices
# what is the minimum number o fpizzas needed - Use floor division

num_of_people = int(input('Please enter in number of people eating:'))
num_of_slices = int(input('Please enter in the number of slices each person will eat:'))
total_slices = num_of_people * num_of_slices
number_of_pizzas = (total_slices + 5)//6
slices_left = number_of_pizzas * 6 - total_slices

print('Number of pizzas order:',number_of_pizzas, 'Number of slices left:',slices_left)