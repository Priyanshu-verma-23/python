# 4. Write a Python program to calculate the sum of three given numbers. If the values are equal,
#  return three times their sum

Num1 = int(input("enter your first number = "));
Num2 = int(input("enter your second number = "));
Num3 = int(input("enter your third number = "));
sum = Num1 + Num2 + Num3;



if(Num1 == Num2 and Num2 == Num3):
    newsum = sum * 3;
    print(newsum);

else:
   
    print("sum of 3 digits are = ", sum);