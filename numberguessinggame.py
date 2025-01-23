import random
top=input("enter a number:")
if top.isdigit():
    top=int(top)
    if top<=0:
        print("Please enter a number greater than or equal to zero")
else:
    print("please enter a number")  
    quit()     
r=random.randint(0,top)
c=0#counter

while True:

    c+=1
    if c<=3:
        guess=input("Make a guess:")
        if guess.isdigit():
            guess=int(guess)
        else:
            print("Please enter a number")
            quit()
        if guess==r:
            print("You got it!") 
            break
        elif guess>top:
            print("Too high")
        else:
            print("Too low")
    
    else:
        print("Retry the game")
        break
 