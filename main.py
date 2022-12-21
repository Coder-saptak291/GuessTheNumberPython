import random

n = random.randint(1,100)
g = int(input("Enter your Guess: "))
nog = 1

while(g!=n):
    if(g>n):
        print("Enter a bit smaller number.")
    elif(n>g):
        print("Enter a bit greater number.")
    g = int(input("Enter your Guess: "))
    nog+=1

print(f"You guessed it in {nog} attempts.")
