from random import randint
from rich.console import Console

console = Console()

streak = 0
missStreak = 0

contin = ''

#console.rule("[bold red]Chapter 2")

while contin != 'quit':
    randColor = randint(1,2)
    
    if randColor == 1:
        color = 'Red'
        console.print(' ' + color + ' ', style='red on black')
    else:
        color = 'Black'
        console.print(' ' + color + ' ', style='black on white')
    currColor = input('Enter "r" or "b" for red or black \n')
    if currColor == 'r':
        currColor = 'Red'
    else:
        currColor = 'Black'
    if currColor == color:
        streak += 1
        missStreak = 0
    else:
        streak = 0
        missStreak += 1
    if streak > 3:
        console.print('Streak: [bright_magenta]{}'.format(streak))
        console.print('Bet on [underline]opposite!!!')
    else:
        print('Streak: {}'.format(streak))

    if missStreak > 3:
        console.print('Miss Streak: [bright_magenta]{}'.format(missStreak))
        console.print('Bet on [underline]same color!!!')
    else:
        print('MissStreak: {}'.format(missStreak))
    contin = input('Press enter to continue or type "quit" to quit the game. \n')
