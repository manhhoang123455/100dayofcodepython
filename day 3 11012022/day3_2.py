print("Welcome to the rollercoaster!!!")
height = int(input("What is your height in cm???"))
bill = 0
if height > 120:
    age = int(input("How old are you???"))
    if age < 12:
        bill = 5
        print("Pay 5$")
    elif age <18:
        bill = 8
        print("Pay 8$")
    else:
        bill =12
        print("Pay 12$")
    photo = input("Do you want to take a photo??")
    if photo == "Y":
        bill +=3
        print(f"total of bill: {bill}$")
    else:
        print(f"final bill {bill}$")
else:
    print("you need to go to home")