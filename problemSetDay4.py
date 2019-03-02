# file name: problemSetDay4.py
player = input('rock (r), paper (p), or sissors (s)?')
print(player, 'vs')
from random import randint
chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)
if player == computer:
    print('draw')
elif player == 'r' and computer == 's':
    print('Player wins!')
elif player == 's' and computer == 'r':
    print('Computer win!')
elif player == 'p' and computer == 'r':
    print("Computer wins!")
elif player == 'r' and computer == 'p':
    print("Player wins!")
elif player == 's' and computer == 'p':
    print('Computer wins!')
elif player == 'p' and computer == 's':
    print('Player wins!')
    