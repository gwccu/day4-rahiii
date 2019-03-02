# file name: problemSetDay4.py
player = input('rock (r), paper (p), or sissors (s)?')
print(player, 'vs', end=' ')
from random import randint
chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer - 's'

print(computer)
if player == computer:
    print('draw)')
