import random
words=["python","alpha","code","game","hangman"]
word=random.choice(words)
display=["_"]*len(word)
guessed=[]
wrong=0
limit=6
print("welcome to Hangman!")
while(wrong<limit and "_" in display):
    print("\nword:"," ".join(display))
    guess=input("enter a letter:").lower()
    if guess in guessed:
        print("Already guessed!")
    else:
        guessed.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    display[i]=guess
        else:
                wrong+=1
                print("wrong! chances left:",limit-wrong)
if "_" not in display:
    print("\n you won! The word was:",word)
else:
    print("\n You lost! The word was:",word)
