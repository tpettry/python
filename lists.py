#Lists
#empty list would be variable = []

data = [53,76,25,98,56,42,69,81]

# data[0]

# x = 1

# print(data[0]);
# this prints the data list in single line with a space
# for num in data:
#     print(num,end=' ')

#Sum connects of list
# total = 0
# for num in data:
#     total = total + num
# print('The sum of \'data\' is:' , total)


#python has a built in sum function 

total_2 = sum(data)
print('total_2 =', total_2)

find_max = 0
for num in data:
    if num > find_max:
        find_max = num
print('Max value is', find_max)

print('Max value using python function', max(data))

my_list = [1,11,21,31,41,51]
for i in range(5):
    print(my_list[i], end =' ')
    print(my_list[i+1])
    print()

#List + For Loop = Powerful Combination
#this is bubble sort and is inefficient.  Python is a sort function that will go over later
data_copy = data[:]
for i in range(len(data_copy)):
    for i in range(0, len(data_copy)-i-1):
        if data_copy[i] > data_copy[i+1]:
            data_copy[i],data_copy[i+1] = data_copy[i+1], data_copy[i]
print(data_copy)
print(sorted(data))
