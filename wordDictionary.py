menu=0
w_means={}
scores=[]
ranks=[]
while True:
    
    print("*************************************************")
    print("*              Sookmyung Dictionary             *")
    print("*************************************************")
    print("               1.Save words                      ")
    print("               2.Delete words                    ")
    print("               3.Print all words                 ")
    print("               4.Search word                     ")
    print("               5.Word Test                       ")
    print("               6.Show Test score                 ")
    print("               7.Exit                            ")
    print("=================================================")

    menu=int(input("Select >> "))
    if menu==1:
        print("Enter word to save. Press 'Enter' to finish")
        while True:
            print("\nWord : ",end='')
            word=input()
            if len(word)==0:
                break
            else:
                if word in w_means:
                    print("Already Exist")
                    print()
                else:
                    print("Mean : ",end='')
                    mean=input()
                    w_means[word]=mean

    if menu==2:
        print("Enter word to deleted")
        while True:
            print("\nWord : ",end='')
            del_word=input()
            if del_word not in w_means:
                print("No such words")
                
            else:
                del w_means[del_word]
                print("Deletion is completed")
                break
    elif menu==3:
        for word, mean in w_means.items():
            print(word,"\t",mean)
                
        
    elif menu==4:
        print("Enter word to search")
        print("\nword : ",end='')
        sr_word=input()
        if sr_word in w_means:
            print()
            print(sr_word,"\t",w_means[sr_word])
    elif menu==5:
        score=0
        if len(w_means)==0:
            print("Test can't be started, because of no words")
        else:
            for word in w_means.keys():
                print(word,end='')
                answer=input(": ")
                if answer==w_means[word]:
                    print("Correct!\n")
                    score=score+1
                else:
                    print("Wrong..\n")
                    score=score 
            print("You got ",score,"answers")
            scores.append(score)
    elif menu==6:
        scores.sort(reverse=True)
        rank=1
        new_list=scores[:]
        for score in scores:
            ranks.append(rank)
            del new_list[0]
            if score in new_list:
                rank=rank
            else:
                rank=len(scores)-len(new_list)+1
        print("     ScoreBoard      ")
        print("=====================")
        for rank in ranks:
            a=ranks.index(rank)
            print(rank," rank\t",scores[a],"answers")
            
   
    elif menu==7:
        print("Thanks for using dictionary")
        break
