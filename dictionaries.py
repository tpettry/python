#dictionaries lesson
# list are mutable; dictionaries are mutable; tuples are immutable; strings are immutable
 
# capitals = {'France':'Paris', 'Spain':'Madrid', 'United Kingdom':'London', 'India':'New Delhi', 'United States':'Washington DC'
#              ,'Italy':'Rome', 'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens','Bulgaria':'Sofia','Ireland':'Dublin'
#              ,'Mexico':'Mexico City'}
 
# #add values to a dictionary
# capitals['South Korea'] = 'Seoul'

# print(capitals['South Korea'])

# #this will print out what is in the dictionary

# print(capitals.items())

# #we can for loop through dictionary
# for country in capitals:
#     print(country)
    
# for country, city in capitals.items():
#     print(f'The capital of {country}, is {city}')
    
#First paragraph of the course to conduct char counts with python

import matplotlib.pyplot as plt

pythonpara = '''This Python course is different. It will not only teach you Python, 
it will give you a problem solving super-power using Python code! 
And that will make all the difference, especially if you are pursuing a career in data science, 
AI, web development, big data, web testing, or programming for smart devices in Python.'''

letter_count = {}
for letter in pythonpara:
    letter_count[letter.lower()] = letter_count.get(letter,0) +1

print(letter_count)

# x,y = zip(*letter_count.items())

# plt.bar(x,y)
# plt.show()

#this will clean up and only show letter counts

# letter_count_clean = {}

# for k,v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k] = v

# print(letter_count_clean)

# x,y = zip(*letter_count_clean.items())

# plt.bar(x,y)
# plt.show()

#this will join the two list together

my_list_1 = [1,2,3,4]
my_list_2 = ['a','b','c','d']

joined = list(zip(my_list_1,my_list_2))
print(f'The result of the zip function {joined} it is of type {type(joined)}')

#split option

new_words = pythonpara.split(' ')

print(new_words)

for i in range(len(new_words)):
    new_words[i] = new_words[i].strip('\n')
    
print(new_words)

# more than one demension

my_list = [[1,2,3], [4,5,6],[7,8,9]]

#this would print the first element which is 1,2,3
print(my_list[0])

#a new dictionary where the first value is a key

countries = {'France':{'Capital':'Paris','Language':'French'}, 'Spain':{'Capital':'Madrid','Language':'Spanish'}}
#this will print key value pairs based on a key
print(countries['France'])

for key, value in countries.items():
    print(key, value)

for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}')