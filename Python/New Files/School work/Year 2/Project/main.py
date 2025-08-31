import random

D={}                                    #Empty dictionary for maximum scores

print("You will be awarded +10 for every correct guess and -3 for every wrong guess. Total 7 chances will be provided!")
ans = 'Y'

while ans == 'Y':
    a=input('''
Choose a theme:- 
    1. FRUITS
    2. TRANSPORT
    3. FLOWERS
    4. INDOOR GAMES
Enter your choice: ''')
    if a not in ['1','2','3','4']:
        print('Invalid input! Try Again...')
    else:
        dash_count = 0
        name = input("Enter Player Name: ")
        print(f'So, {name}, let the game begin!')
        score = 0
        chance = 7

    def func1(v, ML, m11):      #Keeps a check on scores and answers
        global chance
        global dash_count
        global score
        New = ''
        if m11 not in ML:
            if m11 in v:
                for i in range(len(v)):
                    if m11 == v[i]:
                            ML[i] = m11
                            chance -= 1
                            score += 10  
                print("Correct,", name, "! You are doing great!")
                print(chance, 'chances left!')
                print("Score: ", score)
                D[name] = score
                print('\n')
                for i in ML:
                        New += i
                        Main = New
                print(New)
            elif m11 not in v:
                print('Wrong Guess! Try Again')
                chance -= 1
                dash_count += 1
                score -= 3
                print(chance, 'chances left!')
                print("Score: ", score)
                print('\n')
                D[name] = score
        else:
            print(m11, 'is already present in the word! Guess another letter!')
            chance -= 1
            dash_count += 1
            score -= 3
            
    def declare(ML,dash_count):             #Concluding statement of the game
        for i in ML:
            if dash_count==0:
                print("You Won",name,"!!")
                break
            elif dash_count!=0:
                print("You Lost",name,"!!")
                Word()
                print("Better luck next time!")
                break
        
        
        
    def fill_space(v,ML):                   #Guessing the letter
        global dash_count
        global chance
        for i in ML:
            if i=='_':
                dash_count+=1
        while chance<=7:
            if dash_count>0:
                if chance>0:
                    m11=(input('Guess the letter: ')).upper()
                    if m11 not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        print('INVALID INPUT!! TRY AGAIN... ')
                        
                    else:
                        func1(v,ML,m11)
                        dash_count-=1
                    
                if chance==0:
                    declare(ML,dash_count)
                    break
            else:
                declare(ML,dash_count)
                break

    def HighScore():                        #Keeps a record of the high scores
        max=0
        for i in D:
            x=D.get(i)
            if x>max:
                max=x
        for j in D:
            if D[j]==max:
                print(j,'scored the highest score of',max)

    def Word():                            #Displays correct word if the player loses the game
        global a  
        if a=='1':
            print('The correct word is: ',F)
        if a=='2':
            print('The correct word is: ',T)
        if a=='3':
            print('The correct word is: ',FL)
        if a=='4':
            print('The correct word is: ',S)
            

    if a=='1':                                           #FRUITS
        f_list=['MANGO','GRAPES','PEAR','ORANGE','FIGS']
        F=random.choice(f_list)
        if F=='MANGO':
            Main1=('_ A _ _ O')
            print(Main1)
            v1=['M',' ',' ',' ','N',' ','G',' ',' ']
            ML1=list(Main1)
            fill_space(v1,ML1)
           
        if F=='GRAPES':
            Main2=('_ _ A _ E _')
            print(Main2)
            v2=['G',' ','R',' ',' ',' ','P',' ',' ',' ','S']
            ML2=list(Main2)
            fill_space(v2,ML2)

        if F=='PEAR':   
            Main3=('_ E A _')
            print(Main3)
            v3=['P',' ',' ',' ',' ',' ','R']
            ML3=list(Main3)
            fill_space(v3,ML3)
                
        if F=='ORANGE':    
            Main4=('O _ A _ _ E')
            print(Main4)
            v4=[' ',' ','R',' ',' ',' ','N',' ','G',' ',' ']
            ML4=list(Main4)
            fill_space(v4,ML4)
                
        if F=='FIGS':    
            Main5=('_ I _ _')
            print(Main5)
            v5=['F',' ',' ',' ','G',' ','S']
            ML5=list(Main5)
            fill_space(v5,ML5)
    if a=='2':                                     #TRANSPORT
        t_list=['TAXI','SKATEBOARD','TRUCK','SHIP','SUBWAY']
        T=random.choice(t_list)
        if T=='TAXI':
           Main1=('_ A _ I')
           print(Main1)
           v1=['T',' ',' ',' ','X',' ',' ']
           ML1=list(Main1)
           fill_space(v1,ML1)
        
        if T=='SKATEBOARD':
           Main2=('_ _ A _ E _ O A _ _')
           print(Main2)
           v2=['S',' ','K',' ',' ',' ','T',' ',' ',' ','B',' ',' ',' ',' ',' ','R',' ','D']
           ML2=list(Main2)
           fill_space(v2,ML2)

        if T=='TRUCK':
           Main3=('_ _ U _ _')
           print(Main3)
           v3=['T',' ','R',' ',' ',' ','C',' ','K']
           ML3=list(Main3)
           fill_space(v3,ML3)

        if T=='SHIP':
           Main4=('_ _ I _')
           print(Main4)
           v4=['S',' ','H',' ',' ',' ','P']
           ML4=list(Main4)
           fill_space(v4,ML4)

        if T=='SUBWAY':
           Main5=('_ U _ _ A _')
           print(Main5)
           v5=['S',' ',' ',' ','B',' ','W',' ',' ',' ','Y']
           ML5=list(Main5)
           fill_space(v5,ML5)

    if a=='3':                                  #FLOWERS
        fl_list=['JASMINE','FLAME TIP','DAISY','MARIGOLD','SUNFLOWER']
        FL=random.choice(fl_list)
        if FL=='JASMINE':
           Main1=('_ A _ _ I _ E')
           print(Main1)
           v1=['J',' ',' ',' ','S',' ','M',' ',' ',' ','N',' ',' ']
           ML1=list(Main1)
           fill_space(v1,ML1)
        
        if FL=='FLAME TIP':
           Main2=('_ _ A _ E  _ I _')
           print(Main2)
           v2=['F',' ','L',' ',' ',' ','M',' ',' ',' ',' ','T',' ',' ',' ','P']
           ML2=list(Main2)
           fill_space(v2,ML2)

        if FL=='DAISY':
           Main3=('_ A I _ _')
           print(Main3)
           v3=['D',' ',' ',' ',' ',' ','S',' ','Y']
           ML3=list(Main3)
           fill_space(v3,ML3)

        if FL=='MARIGOLD':
           Main4=('_ A _ I _ O _ _')
           print(Main4)
           v4=['M',' ',' ',' ','R',' ',' ',' ','G',' ',' ',' ','L',' ','D']
           ML4=list(Main4)
           fill_space(v4,ML4)

        if FL=='SUNFLOWER':
           Main5=('_ U _ _ _ O _ E _')
           print(Main5)
           v5=['S',' ',' ',' ','N',' ','F',' ','L',' ',' ',' ','W',' ',' ',' ','R']
           ML5=list(Main5)
           fill_space(v5,ML5)

    if a=='4':                                  #INDOOR GAMES
        s_list=['LUDO','DART','UNO','POKER','BINGO']
        S=random.choice(s_list)
        if S=='LUDO':
           Main1=('_ U _ O')
           print(Main1)
           v1=['L',' ',' ',' ','D',' ',' ']
           ML1=list(Main1)
           fill_space(v1,ML1)
        
        if S=='DART':
           Main2=('_ A _ _')
           print(Main2)
           v2=['D',' ',' ',' ','R',' ','T']
           ML2=list(Main2)
           fill_space(v2,ML2)

        if S=='UNO':
           Main3=('U _ O')
           print(Main3)
           v3=[' ',' ','N',' ',' ']
           ML3=list(Main3)
           fill_space(v3,ML3)

        if S=='POKER':
           Main4=('_ O _ E _')
           print(Main4)
           v4=['P',' ',' ',' ','K',' ',' ',' ','R']
           ML4=list(Main4)
           fill_space(v4,ML4)

        if S=='BINGO':
           Main5=('_ I _ _ O')
           print(Main5)
           v5=['B',' ',' ',' ','N',' ','G',' ',' ']
           ML5=list(Main5)
           fill_space(v5,ML5)

    ans=(input("Do you want to play again? Enter 'Y' for Yes and 'N' for No ").upper())
    if ans!='Y':
        HighScore()
