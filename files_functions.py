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

f = open('kipling.txt','r')

print(f.readline())

f.close()