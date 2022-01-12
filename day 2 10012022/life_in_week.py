age = int(input("What is your current age?\n"))

day = 90*365 - age*365

week = day//7

month = week//4

print(f"you have {day} days, {week} weeks,and {month} months left")