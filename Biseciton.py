# Finger Exercise 6
# Name: Mustafa Sabri Derbent
# Collaborators: -
# Time Spent: 20 minutes 33 seconds

#Mine
N = int(input("Enter a secret number 1-1000\nSHSHH! Don't let him hear! "))
high = 1000
low = 0
tahmin = (high+low)/2
sayac = 1
while tahmin != N:
    sayac += 1
    if tahmin <= N:
        low = tahmin
    elif tahmin > N:
        high = tahmin
    tahmin = (high+low)/2 
print(f'Guess amount: {sayac}')
print(f'Your secret number is {N}!')
    
#Solution
low = 0
high = 1001  # its now includes 1000
guess = (high+low)//2
count = 1
while guess != N:
    count += 1
    if guess < N:  # no need for "="
        low = guess
    elif guess > N:
        high = guess
    guess = (high+low)//2 # for even numbers also
    
print('count:', count)
print(f'Your secret number is {guess}!')
    
    