# 11. Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

a = int(input("enter your number = "));

if ((a == 1) or (a == 5) or (a == 8) or (a == 3)):
    print("number in a group");

else:
    print("number is not in group");

