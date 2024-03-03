num1 = int(input("enter your first number = "));
num2 = int(input("enter your first number = "));

def divide():
            div = 1;
            if((num1 % div == 0) and (num2 % div == 0)):
                 gcd = div;
                 div = div + 1;
                 if(div <= num2):
                        divide();
                                        

            else:
                 div = div + 1;
                 divide();

if(num1 > num2):
    breakr = num2;
    
    divide();

    
        

        