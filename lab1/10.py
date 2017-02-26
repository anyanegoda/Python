import re

password = input("Enter password: ")
n = 0
if len(password) >= 8:
    n += 1
if re.search(r'[0-9]', password):
    n += 1
if re.search(r'[A-Z]', password):
    n += 1
if re.search(r'[a-z]', password):
    n += 1

if n == 1 or n == 2:
    print("Password is Weak.")
if n == 3:
    print('Password is Medium.')
if n == 4:
    print('Password is Strong.')