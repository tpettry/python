#Python standard library to access these files called modules
#this import pulls in the math module and dir shows what the module contains also look at the 
# official python documentation https://docs.python.org/3/library/math.html#module-math
# import math

# print(dir(math)) 
 
# print(math.pi)

# this will print random integers and the for loop provides 100 random values also we can do an alias to 
import random as r

print(r.randint(1,100))

for i in range(100):
    print(r.randint(1,100), end= ' ')

