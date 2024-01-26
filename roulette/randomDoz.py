from random import randint

keepPlaying = 1
streak = 0

while keepPlaying != '0':
    randDoz = randint(1, 3)
    print('randDoz: {}'.format(randDoz))
    currentDoz = int(input('Enter current Dozen: \n'))
    if currentDoz == randDoz:
        streak += 1
    else:
        streak = 0
    print('Streak: {}'.format(streak))
    keepPlaying = input('To continue press Enter, otherwise press 0 \n')
    
