import random
print("Word Guess Game")
word_bank = ['Virat','Dhoni','Rohit','Ruturaj']
word = random.choice(word_bank)
gussedword = ['_\t']*len(word)
attempts =10
while attempts>0:
    print('\ncurrent word:'+''.join(gussedword))
    guess=input('Guess a letter:')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                gussedword[i]=guess
        print('Great Guess Boss!')
    else:
        attempts-=1
        print("Wrong Guess....Attempt Failed! Attempts left:"+str(attempts))
    if '_' not in gussedword:
        print('Congratulations!...You gussed the word:'+word)
        break
else:
    print("Lost all the attempts... Word was:"+word)
