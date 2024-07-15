# Finger Exercise 4
# Name: Mustafa Sabri Derbent
# Collaborators: -
# Time Spent: 15 minutes 55 seconds


# Spent 8 minutes couldn't able to figure out
# N = int(input('Enter a number to compute its cube root: '))
# üst = N
# alt = 0
# tahmin = (üst + alt)/2 
# epsilon : 0.1
# for i in range(10):
#     if tahmin > N:

N = int(input('Enter a number to compute its cube root: '))
i = 0
while i**3 < N:
    i += 1
if i**3 == N:
    print(f'Cube rooted {N} is {i}')
else:
    print('error')