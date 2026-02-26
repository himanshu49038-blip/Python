import random
def game():
    num = random.randint(1,100)
    a = 0
    while(True):
        g = int(input("Enter your guess: "))
        a+=1
        if(g > num):
            print("Too high!! try again")
        elif(g < num):
            print("Too low!! try again")
        else:
            print("Congratulation!! Correct")
            print("Total attempt taken:  ",a)
            break
while True:
    game()
    ans = input("Do you want to play again? (yes/no):  ")
    if ans != "yes":
        print("Thank you for playing!!")
        break