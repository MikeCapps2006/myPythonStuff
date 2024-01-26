from random import randint

randNum = randint(1,100)
guessCounter = 0
guessing = True

# print(randNum)
while guessing == True:
    guess = int(input('Guess an integer from 1 - 100...  '))
    if guess > 100 or guess < 1:
        print('OUT OF BOUNDS!!! --- Integer has to be from 1 - 100')
        continue
    guessCounter += 1

    if guess == randNum:
        print('you guessed right')
        print(f'it took you {guessCounter} guess(s)')
        guessing = False
    else:
        if guessCounter == 1:
            if abs(randNum - guess) > 10:
                print('Cold!!')
            else:
                print('Warm!!')
            prevGuess = guess
        else:
            if abs(guess - randNum) < abs(prevGuess - randNum):
                print('Warmer!!!')
            else:
                print('Colder!!!')
            prevGuess = guess
        
        print('you guessed wrong try again \n')