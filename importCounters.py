#import counters

pythonpara = '''This Python course is different. It will not only teach you Python, 
it will give you a problem solving super-power using Python code! 
And that will make all the difference, especially if you are pursuing a career in data science, 
AI, web development, big data, web testing, or programming for smart devices in Python.'''

from collections import Counter

print(Counter(pythonpara.lower()))

#will convert counter to dictionary

new_dict = dict(Counter(pythonpara.lower()))

#dictionary comprehension

new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}

print(new_dict)