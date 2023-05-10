## ability to call functions from another file

import functions

functions.fib_2(10)

## function can have multiple things that would turn into a tuple that you can unpack

def sum_and_mult(a,b):
    total = a + b
    product = a * b
    
    return total, product

print(sum_and_mult(1,4))


# could have multiple values assign to many variables

var_1, var_2 = sum_and_mult(6,7)

print(var_1)
print(var_2)