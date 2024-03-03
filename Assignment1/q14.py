#19. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.


num1 = int(input("enter the first num = "));
num2 = int(input("enter the second num = "));
num3 = int(input("enter the third num = "));

sum = num1 + num2 + num3;

if((num1 == num2) or (num2 == num3) or (num1 == num3)):
    print('0');

else:
    print(sum); 
