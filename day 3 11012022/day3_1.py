number = int(input("which your number do you want to check???"))

if number%2==0:
    print("this is an even number")
    age = int(input("How old are you??"))
    if age > 18:
        print('the ticket have a 12$')
    else:
        print('The ticket have a 8$')
else:
    print("This is an odd number")