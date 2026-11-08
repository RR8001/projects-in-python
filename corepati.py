#kyon banega corepati

print("Welcome to kyon banega corepati")
print("Alert! you have to give all answers correct in oreder to win one crore")

    
    






questions = ["What does the acronym HTTP stand for in a website address?",
        "Which company developed the Android mobile operating system?",
        "What was the name of the first commercially available electronic digital computer?",
        "Which programming language is symbolized by a coffee cup logo?"]

options =[
        [ "HyperText Transfer Protocol", "HighText Transfer Program", "Hyper Transfer Text Process", "Hyperlink Transmission Protocol"],
        ["Apple", "Microsoft", "Google", "IBM"],
        ["ENIAC", "UNIVAC", "EDSAC", "EDVAC"],
     ["Python", "Java", "C++", "JavaScript"]
    ]

answers = ["hypertext transfer protocol",
        "google","eniac",
        "java"]

prize = [1000000,2000000,2000000,5000000]
prizes =0
while True:
    for i in range(len(questions)):

        print('\n questions:',questions[i])
        print(options[i])
        ans_1 = input("enter your answer").lower().strip()
        if ans_1 == answers[i]:
            prizes =int(prize[i]) + prizes
            print("you won:Rs",prizes)

        else:
            print("you loose all your money")
            print("It's fine! next time do better!")
            interest= int(input("if you want to try again press 1"))
            if interest != 1:
                break
        if prizes == 10000000:
            name = input("enter your name")
            print(f"congrats! {name} , you are our crorepati")
            break
    

    
          
         




    