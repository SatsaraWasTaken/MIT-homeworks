# Problem Set 0
# Name: Mustafa Sabri Derbent
# Collaborators: -
# Time Spent: 27 minutes

a = 1
b = -5
c = 6
root_1 = (-b + (b**2 -4*a*c)**0.5)/2*a
root_2 = (-b - (b**2 -4*a*c)**0.5)/2*a

def is_positive(a):
    if a > 0:
        return True
    else:
        return False
    
if is_positive(root_1) and is_positive(root_2) :
    print(f'Positive roots of the equation are:\n{root_1} and {root_2}')  # "alt+92" for \, \n alike enter 
elif root_1 > root_2 and is_positive(root_1):
    print(f'Positive root of the equation is:\n{root_1}')
elif root_2 > root_1 and is_positive(root_2):
    print(f'Positive root of the equation is:\n{root_2}')
else:
    print('There are no positive roots of the equation')
