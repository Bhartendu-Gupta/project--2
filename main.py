import random
n=random.randint(1,100)
a=-1
guessess=0
while(a!=n):
    guessess=1
    a=int(input("guess the number:"))
    if(a>n):
        print("Lower no please")
        guessess+=1
    elif(a<n):
        print("Higher no please")
        guessess=+1
        
print(f"You have Guessed the no {n} correctly in {guessess} attempts")