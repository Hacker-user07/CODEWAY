questions=("What country has the highest life expectancy?",
           "Where would you be if you were standing on the spanish steps?",
           "Which language has the more native speakers?",
           "What is the most common surname in United States?",
           "WHat disease commonly spread on pirate ships?")

MCQS=(("A.China","B.India","C.Russia","D.Hong Kong"),
      ("A.Rome","B.Barcelona","C.Madrid","D.seville"),
      ("A.English","B.Spanish","C.Japanaese","D.Hindi"),
      ("A.Wick","B.Smith","C.Margos","D.Leonardo"),
      ("A.Scurvy","B.Influenza","C.Measles","D.Alzheimer"))
qnum=0
answer=("D","A","B","B","A")
userAnswer=[]
score=0
for i in questions:
    print("------------------------------------------")
    print(i)
    for j in MCQS[qnum]:
        print(j)
    ans=input('Enter your option:').upper()
    userAnswer.append(ans)
    if ans==answer[qnum]:
        print("Correct")
        score+=1
    else:
        print('Incorrect')
    qnum+=1

result=int(score/len(questions)*100)
print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")
print("Your score is:",result)
print("Answers:",answer)
print("Your Answer:",userAnswer)