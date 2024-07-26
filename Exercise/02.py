import Questions

questions=Questions.questions

Number=len(questions)
score=0
for i in range(Number):
    Answer=''
    # print(f"\n{questions[i]['No']}",". ",end='')
    print(f"{questions[i]["Question"]}\n")
    print(f"A) {questions[i]["A"]}\n")
    print(f"B) {questions[i]["B"]}\n")
    print(f"C) {questions[i]["C"]}\n")
    print(f"D) {questions[i]["D"]}")
    print("")
    Answer=input("Enter Your Answer : ")
    
    if(Answer.upper()==questions[i]['Ans']):
        print("Your answer is correct")
        score+=1
    else:
        print("Your Answer was wrong")
        # print(f"Correct answer is {questions[i]['Ans']}")
        print(f"Correct answer is {questions[i]['Ans']}) {questions[i][questions[i]['Ans']]}")
    print("")
    
print(f"||||||||||||||| Score : {score}/{len(questions)} |||||||||||||||")