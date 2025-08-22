from random import randint
print("\t✨ WELCOME TO 🎮 THE PERFECT GUESS GAME 🕹️")
n=randint(1,100)
guesses=0
a=-1
while(a!=n):
    guesses+=1
    a=int(input("Enter your number here :- "))
    if(a<0):
        print("❌You enter the negativem number.\nPlease enter the right number !!")
        continue
    if(a<n):
        print("⬆️  Higer number please !!")
    elif(a>n):
        print("⬇️  Lower number please !!")
print(f"🎉WOW!! you guess the right number \"{n}\" and you take {guesses} attempts.")        
