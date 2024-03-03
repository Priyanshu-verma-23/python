import random

a= int(input('enter your number = '));
b = random.randint(1, 10);

if(a == b):
    print('you won');

else:
    print('you lose');
    print('number is ',b);