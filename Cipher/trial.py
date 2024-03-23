from cipher import *
link = input('Enter the full link of the file--')
with open(link,"+r") as f:
    encoded = encode(f.readline())
    print(f'The encoded text is : {encoded}\n')
    decoded = decode(encoded)
    print(f'The decoded text is : {decoded}\n')    