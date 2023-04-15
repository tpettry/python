#going over some list methods

my_list = [34,76,58]

my_list.append(100)
my_list.remove(34)
my_list.extend([67,68,69])

print(sorted(my_list))

#while loop Dot notation is an integral part of Python coding

# n = 10
# while n > 0:
#     print(n, end = ' ')
#     n = n-1

# user_input = int(input('Please enter ages of class member, Type -1 to stop the code entry'))
# ages = []
# while user_input > 0:
#     ages.append(user_input)
#     user_input = int(input('The next age:>'))
# print('The ages are',ages, end = ' ')

#f string with {} allows to print a string with a variable in it
count = 0
class_names = []
name = input('Please enter name type n to stop:> ')
while name != 'n':
    count +=1
    class_names.append(name)
    print(f'{name} has been added.')
    name = input('Next name?:> ')


print(f'There are {count} people in the class, they are {class_names}')
