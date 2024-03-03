witha = input("press w for withdraw money = ");
def inbank():
     money = int(input("enter your money = "));
     if((money % 100 == 0) or (money % 500 == 0)):
           print("you successfully withdraw your money = ", money);
     else:
           print("press the valid money amount which should be multiple of 100");




if(witha == 'w'):
    pin = int(input("enter your pin for withdraw money = "));
    if(pin == 1232):
         inbank();
    else:
         print("Wrond pin ! Try Again");
         pin = int(input("enter your pin for withdraw money = "));
         if(pin == 1232):
            inbank();
         else:
             print("Wrond pin ! Try Again");
             pin = int(input("enter your pin for withdraw money = "));
             if(pin == 1232):
                 inbank();
             else:
                  print("Your Atm card is block for 24 hours");


else:
     print("you press wrong key");


