import random
print("Welcome to the Number Guessing Game!")
#generate a random number between 0 and 100
number=random.randint(0,100)
numberguessed=int(input("Enter a number from 0 to 100: "))
if numberguessed>=0 and numberguessed<=100:
    for i in range(7):
        if numberguessed > number :
            print("too hight,try again!")
            numberguessed=int(input("Enter a number from 0 to 100: "))
        elif numberguessed < number :
            print("too low ,try again!")
            numberguessed=int(input("Enter a number from 0 to 100: "))
        else:
            print("you won!")
            break
    if i==6 and numberguessed != number:
        print("you lost! the number was:",number) 
    else:
        print("you won!")      
else:
    print("Invalid input. Please enter a number between 0 and 100.")                

