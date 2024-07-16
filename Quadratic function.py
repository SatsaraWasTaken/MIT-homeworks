# Finger Exercise 7
# Name: Mustafa Sabri Derbent
# Collaborators: -
# Time Spent: 11 minutes 06 seconds

a = int(input('Enter an a '))
b = int(input('Enter a b '))
c = int(input('Enter a c '))
x = int(input('Enter an x '))

def eval_quadratic(a,b,c,x):
    if a != 0:
        return ((a*x**2)+(b*x)+c)
    else:
        return False

print(eval_quadratic(a, b, c, x))
