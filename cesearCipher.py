# Lesson on encrypting messages and decrypting messages
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_text = 'hello'

def shift_amount(i):
    return i%26

# output = ''
# for char in input_text:
#     alpha_index = alphabet.find(char)
#     output = output + alphabet[alpha_index+5]
# print(output)




# #encryption
def encrypt (text, required_shift):
    out_string = ' '
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index +required_shift)]
    return out_string

newWord = encrypt('Hello World!', 5)
print(newWord)

basker = """I confess at these words a shudder passed through me. 
            There was a thrill in the doctor's voice which showed that he was himself deeply moved by that which he was told us.  
            Holmes leaned forward in his excitement and his eyes had the hard, dry glitter which shot from them when he was keenly interested."""

encrypt_basker = encrypt(basker, 10)
print(encrypt_basker)

# #decrypt
print(encrypt(encrypt_basker,-10))
# def decrypt (text, num):
#     #some function

#     return decrypt msg
