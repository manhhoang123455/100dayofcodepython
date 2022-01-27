from random import randint

print("chao mung den voi tro choi doan so:")
computer_choice = randint(1,100)

print(computer_choice)

turn = 0

while turn <=7:
    you_choice = int(input("Vui long nhap vao so ban doan: "))
    if you_choice == computer_choice:

        break
    elif you_choice < computer_choice:
        print("So ban doan nho hon:")
    elif you_choice > computer_choice:
        print("So ban doan lon hon:")
    turn == 1

if turn == 8:
    print("You lose")
    print(computer_choice)
else:
    print('You win')
    print(computer_choice)