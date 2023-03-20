# Loops

# For Loops

for i in range(10):
    print(i)

for i in range(10):
    print(i, end=' ')

for i in range(1,10):
    print(i, end=' ')

# this will increment by 4
for i in range(0, 101, 4):
    print(i,end=' ')

#Also can go backwords
for i in range(100, 0, -1):
    print(i,end=' ')

#different example with word

word = 'python'

for i in word:
    print(i)

#typically use char to go through list as i is for index values

word = 'python'

for char in word:
    print(char)
