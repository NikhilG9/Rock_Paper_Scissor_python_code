import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
    
    
    
    

import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='r':
            return True
        elif you =='p':
            return False
    elif comp=='r':
        if you=='p':
            return True
        elif you =='s':
            return False
    elif comp=='p':
        if you=='s':
            return True
        elif you =='r':
            return False
        
k= int(input("For how many time do you wish to play the game:  "))   
for i in range (k):
    print('''Comp chosses from r,p,s, wherer: 
    \n
    r=rock
    p=paper
    s=scissor
    \n''')
    rand=random.randint(1,3)
    if rand==1:
        comp='r'
    elif rand==2:
        comp='p'
    elif rand==3:
        comp='s'
    you=input("Chosses from r,p,s Now go ==>  ")
    if you =='r' or you =='p' or you =='s':
        a=game(comp,you)
        print("Comp chos: " + comp)
        print("you chos: " + you)
        if a==None:
            print(f":::you have ...{k-1-i}... chance left::: \nit's a tie")

        elif a== True:
            print(f":::you have ...{k-1-i}... chance left::: \nYOU WIN :)")

        elif a==False:
            print(f":::you have ...{k-1-i}... chance left::: \nYOU LOSSE :(")
            
    else:
        print("\n???YOU have played an invalid move!!???\n\t???Please try again:???"+f"\n:::you have ...{k-1-i}... chance left:::")
