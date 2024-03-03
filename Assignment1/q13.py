# 20. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

a = int(input("enter the first number = "));
b = int(input("enter the second number = "));

sum = a + b;

if(sum >=15 and sum<=20):
    print('20');

else:
    print(sum);