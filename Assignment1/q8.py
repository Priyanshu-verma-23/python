# 9. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given
#  string. Return n copies of the whole string if the length is less than 2.

string = str(input("enter your string = "));
lengthOfstring = len(string);

n = int(input("how many copy you want = "));
if(lengthOfstring <= 2):
    copy = n * string;
    print(copy);

else:
    firstTwo = string[0:2];
    copy = n * firstTwo;
    print(copy);





    
