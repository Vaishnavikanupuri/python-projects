import random
computer=0
user=0
options=["rock","paper","scissors"]
while True:
    input1=input("enter your choice:")
    if input1 not in options:
        print("Invalid input.")
        continue
    computer1=random.choice(options)
    if input1==computer1:
        print("It's a tie.")
    elif input1=="rock" and computer1=="scissors":
        user+=1
    elif input1=="paper" and computer1=="rock":
        user+=1
    elif input1=="scissors" and computer1=="paper":
        user+=1
    elif input1=="scissors" and computer1=="rock":
        computer+=1
    elif input1=="rock" and computer1=="paper":
        computer+=1
    elif input1=="paper" and computer1=="scissors":
        computer+=1
    print("Computer:",computer)
    print("User:",user)
    

