name_string = input("give me everybody's names,seperated by a command!!!\n")

names = name_string.split(",")

import random

# c1
# num_item = len(names)

# random_choice = random.randint(0,num_item-1)

# print(f'{names[random_choice]} la nguoi se tra tien')

# c2

person_who_will_pay = random.choice(names)

print(f'{person_who_will_pay} is going to buy the meal today')