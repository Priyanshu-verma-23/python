# 3. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input('enter your number = '));
if(num>0 and num<=100):
    print("number is", num, "lie between 0 to 100");
elif(num>100 and num<=1000):
    print("number is", num, "lie between 100 to 1000");
elif(num>1000 and num<=2000):
    print("number is", num, "lie between 1000 to 2000");