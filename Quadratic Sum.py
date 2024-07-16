# Finger Exercise 7.2
# Name: Mustafa Sabri Derbent
# Collaborators: -
# Time Spent: 10 minutes 21 seconds

a1 = int(input('Enter a number: '))
a2 = int(input('Enter a number: '))
b1 = int(input('Enter a number: '))
b2 = int(input('Enter a number: '))
c1 = int(input('Enter a number: '))
c2 = int(input('Enter a number: '))
x1 = int(input('Enter a number: '))
x2 = int(input('Enter a number: '))

def two_quadratic(a1,b1,c1,x1,a2,b2,c2,x2):
    if a1 != 0 and a2 != 0:
        print(((a1*x1**2)+(b1*x1)+c1) + ((a2*x2**2)+(b2*x2)+c2))
    else:
        return False

print(two_quadratic(a1, b1, c1, x1, a2, b2, c2, x2))