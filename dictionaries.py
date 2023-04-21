#dictionaries lesson
 
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

x,y = zip(*letter_count.items())

plt.bar(x,y)
plt.show()
