#modulus gives you the remainder of the result of the division

x = 10 % 2

print(x)

#FizzBuzz if number divisible by 3 is fizz if divisible by 5 buzz if both it is fizzbuzz
#order of the conditions are important because once one if is true it will stop
n = 100

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz!!!')
    elif i % 5 == 0:
        print(i,'buzz')
    elif i % 3 == 0:
        print(i,'fizz')
    else:
        print(i)
