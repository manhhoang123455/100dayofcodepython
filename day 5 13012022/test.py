import string,random

char = string.ascii_letters
print(char)

password = []
for c in range(4):
    password.append(random.choice(char))

print(password)