# %%
import random as rd 
fib = [0,1,1,2,3,5,8,13,21]
advance_steps = rd.choice(fib)


# %%
def encode(string):
    encoded_str = ''
    for i in string:
        if i.isspace():
            encoded_str += '-'
        else:
            new_char = chr(ord(i) + advance_steps)
            encoded_str += new_char 
    return encoded_str


# %%
def decode(string):
    decoded_str = ''
    for i in string:
        if i == '-':
            decoded_str += ' '
        else:
            old_char = chr(ord(i) - advance_steps)
            decoded_str += old_char
    return decoded_str

# %%



