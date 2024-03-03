# 2. Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.


givenNumber = int(input("enter your number = "));
b = 17;

difference = givenNumber - b;


if(givenNumber>=b):
    newdifference = difference * 2;
    print(newdifference);

else:
    print("difference is = ",  -difference);




