print("welcome to kBC..........")
que=[["how many continents are there?"],
     ["what is the capital of india?"],
     ["which course that NG will provide?"]]
opt=[["four","nine","seven","eight"],
     ["chandigarh","bhopai","chennai","delhi"],
     ["software","counseling","tourism","agricuiture"]]
sol=[["seven","delhi","software"]]
i=0
c=0
while(i<len(que)):
    print(que[i])
    j=0
    while(c<len(opt)):
        while(j<=len(opt)):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line")
    if(life1=="yes"):
        print("1.four","3.seven")
        ans1=input("select opt")
        if(ans1=="seven"):
            print("correct")
            print("your answer is correct so you win rs.1000/-")
            print("your are qualified to the next round")
            print("now the next question is")
        break
    else:
        print("good")
        ans1=input("select opt")
        if(ans1=="seven"):
            print("correct")
            print("your answer is correct so you win RS.1000/-")
            print("your are qualified to the next round")
            print("now the next question is")
        else:
            print("wrong")
            print("sorry your answer is wrong your are disqualified")
        break
i=i+1
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line")
    if life1=="yes":
        print("1.chandigarh","4.delhi")
        ans2=input("select opt")
        if ans2=="delhi":
            print("correct")
            print("your name is correct so you win RS.3000/-")
            print("you are qualified to the next round")
            print("now the next quastion is")
        else:
            print("wrong")
            print("sorry your answer is wrong so your disqualified")
            break
i=i+1
c=0
while(i<len(que)):
    print(que[i])
    j=0
    while(c<len(opt)):
        while(j<len(opt)):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line")
    if(life1=="yes"):
        print("1.software","4.agriculture")
        ans2=input("select option")
        if ans2=="software engineering":
            print("correct")
            print("congrats your answer is correct so you e=win RS.10000/-")
        break
    else:
        print("great")
        ans2=input("select opt")
        if(ans2=="software"):
            print("correct")
            print("congragulation your ans is correct so you win RS.10000")
        else:
            print("wrong")
            print("sorry your ans is wrong so you are dis qualified")  
        break
