import random
name = str(input("Enter your name: "))
question = str(input("Ask your question: "))

if (question == ""):
    print("Ask a question please!!")
    exit
else:
    if (name == ""):
        print(" asks: " + question)
    else:
        print(name + " asks: " + question)
    
        answer = ""
        random_number = random.randint(1, 9)

        if(random_number == 1):
            answer = "Yes - definitely."
        if(random_number == 2):
            answer = "It is decidedly so."
        elif(random_number == 3):
            answer = print("Without a doubt.")
        elif(random_number == 4):
            answer = "Reply hazy, try again."
        elif(random_number == 5):
            answer = "Ask again later."
        elif(random_number == 6):
            answer = "My sources say no."
        elif(random_number == 7):
            answer = "My sources say no."
        elif(random_number == 8):
            answer = "Outlook not so good."
        elif(random_number == 9):
            answer = "Very doubtful."
        else:
            answer = "Error"
  
        print("Magic 8-Ball's answer: " + answer)
