#Files and functions lesson 
#Python can open, close, read to and write to files

#creating a new text file, if you want to w-write, r-read, a-append
# f = open('kipling.txt','w')

# print(type(f))

# f.write('If you can keep your head while all about you \nare losing theirs\
#     and blaming it on you, \n')

# f.write('If you can trust yourself when all men doubt you, \n\
#     But make allowance for their doubting too;\n')

# f.write('If you can wait and not be tired by waiting, \n\
#     Or being lied about, don\'t deal in lies,\n')

# f.write('Or being hated, don\'t give way to hating,\n\
#     And yet don\'t look too good, nor talk to wise:\n')

# f.close()

#read the txt file

# f = open('kipling.txt','r')

# print(type(f))

# print(f.read())
# f.close()

# read the file by line

# f = open('kipling.txt','r')

# print(f.readline())

# f.close()

## this will append to the file
# f = open('kipling.txt', 'a')

# f.write('If you can dream - and not make dreams your master; \n\
#     If you can think - and not make thoughts your aim;\n')
# f.close()
# print()
# f =open('kipling.txt','r')
# print(f.read())
# f.close()
# print()

## This will close the file automatically.  this is the preferred method
with open('kipling.txt','r') as f:
    for line in f.readlines():
        #using end='' will get rid of the space in between the lines 
        print(line,end='')

 