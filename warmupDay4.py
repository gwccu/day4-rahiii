# File name: warmupDay4.py
number = 5
guess = int(input('guess a number'))
while guess != 5:
    print('inncorect')
    guess = int(input('guess a number'))
print('correct!')

playern = int(input('chose a number '))
playerm = int(input('chose an exponent '))
print (playern, 'to the power of', playerm, 'is', playern ** playerm)

n = int(input('chose a number'))
m = int(input('chose an exponent'))
solution = n*m
while solution != n*m:
    print('inncorrect')
    solutuion = n*m

strength = 5
print( 'your strength is', strength)
while strength <= 10:
    print(strength)
    strength += 1
    print('your increasing')
print('your too strong! You have leveled up!')



