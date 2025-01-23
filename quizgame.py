print("Welcome to the quiz game!")
print("Enter our choice:")
choice=int(input())
c=0
match choice:
    case 1:
        print("Animal Quiz!")
        print("You will be asked 3 questions.")
        answer1=input("1.Which animal has the most bones?")
        if answer1=="python":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer2=input("2.How many arms do a starfish have?")
        if answer2=="five":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer3=input("3.Which animal has the most brains?")
        if answer3=="octopus":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        print("Your score is:",c)
    case 2:
        print("Human Body Quiz!")
        print("You will be asked 3 questions.")
        answer1=input("1.How many bones do humans have?")
        if answer1=="206":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer2=input("2.Which organ pumps blood throughout the body?")
        if answer2=="heart":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer3=input("3.What is the name of the organ that helps us digest food?")
        if answer3=="stomach":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        print("Your score is:",c)    
    case 3:
        print("General knowledge Quiz!")
        print("You will be asked 3 questions.")
        answer1=input("1.What is the captial of Bihar?")
        if answer1=="patna":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer2=input("2.Which ocean is the deepest on earth?")
        if answer2=="pacific ocean":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        answer3=input("3.Which is the largest continent on the earth?")
        if answer3=="asia":
            c+=1
            print("Correct!")
        else:
            print("Incorrect!")
        print("Your score is:",c)

