print("Welcome to the Love Caculator!!!")
name1 = input("what is your name? ")
name2 = input("what is your name? ")

char_T = name1.lower().count("t")
char_R = name1.lower().count("r")
char_U = name1.lower().count("u")
char_E = name1.lower().count("e")

char_L = name1.lower().count("l")
char_O = name1.lower().count("o")
char_V = name1.lower().count("v")
char_E = name1.lower().count("e")

total_true = char_T + char_R + char_U + char_E

total_love = char_L + char_O + char_V + char_E

print(f"{total_true}{total_love}")
