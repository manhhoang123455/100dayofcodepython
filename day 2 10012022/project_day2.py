print('Welcome to the tip caculator.')

total_bill = float(input('What was the total bill?\n'))

tip = int(input('What percentage tip would you like to give? 10, 12, 15?\n'))

people = int(input('How many people to split the bill?\n'))

total = total_bill + tip*total_bill/100

each_people_pay = total / people

print(f'Each person should pay: ${each_people_pay}')

