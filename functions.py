## Beginning the lesson of functions

#print('Hello World!')

##creation of your own function using def and the name that you want to call the function
# def hello():
#     print('Hello, world!')

# hello()

# for i in range(5):
#     hello()

## example of a function taking an argument
# def hi(name):
#     print(f'Hello, {name}')

# hi('Giles')

##example of a function taking a key word argument where if a value is not provide it defaults a value

# def hi_2(name='BOFA'):
#     print(f'Hello, {name}!')

# hi_2()
# hi_2('Tim')

##Fibonacci in a function within the function it should contain a docstring to explain what the function does
# n=20
# a=0
# b=1
# for i in range(n):
#     a,b = b,a+b
# print(a)

# def fib(n):
#     '''This function calculates the Fibonacci sequence'''
#     a=0
#     b=1
#     for i in range(n):
#         a,b = b,a+b
#     return a

# fib_num = fib(24)

# print(f'The answer is {fib_num}')

# for i in range(20):
#     print(f'This is the answer{fib(i)}')

##This function with have a * because we want the function to handle a unknown amount of list values

def cal_mean(first, *remainder):
    '''This calculates the mean of numbers'''
    mean = (first + sum(remainder))/ (1+ len(remainder))
    
    return mean
print(cal_mean(23,43,56,76,45))