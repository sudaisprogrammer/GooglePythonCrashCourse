import random

pass_len = int(input("Enter your password length: "))

letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%^&*()_+-{[]},.<>:;~'

# mypass = random.shuffle(letters,capital_letters,numbers,symbols)

allchars = letters+capital_letters+numbers+symbols
newpass = ''
while len(newpass)!=pass_len:
    newpass += random.choice(allchars)
print("password is ",newpass)