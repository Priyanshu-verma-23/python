bjp = 19;
congress = 21;
others = 20;
tmc = 24;
aap = 27;


age = int(input('enter your age = '));
if(age >=18):
    print("you are eligible");
    print("press b for bjp\npress c for congress\npress a for other\npress aap for aap\npress t for tmc");
    party = str(input());
    if(party == 'b'):
        print("you voted to bjp");
        bjp = bjp + 1;
        if(bjp>others and bjp>tmc and bjp>congress and bjp>aap):
                print("vote of bjp is ", bjp);
    elif(party == 'c'):
        print("you voted to congress");
        congress = congress + 1;
        print("vote of congress is ", congress);
    elif(party == 'o'):
        print("you voted to others");
        others = others + 1;
        print("vote of others is ", bjp);
    elif(party == 'b'):
        print("you voted to aap");
        aap = aap + 1;
        print("vote of b is ", aap);
    elif(party == 't'):
        print("you voted to tmc");
        tmc = tmc + 1;
        print("vote of tmc is ", tmc);
       
else:
    print("you are not eligible");








if(bjp <= congress):
    new = bjp + 2000;
    print("vote of bjp is", new);
elif(bjp<=others):
    new = bjp + 2000;
    print("vote of bjp is", new);
elif(bjp <= aap):
    new = bjp + 2000;
    print("vote of bjp is", new);
elif(bjp <= tmc):
    new = bjp + 2000;
    print("vote of bjp is", new);


result = str(input("press y for know the result or n for not = "));
if(result == 'y'):
    print("bjp , tmc, other, aap, congress");
    print(new,tmc, others, aap, congress);

else:
    print("you press wrong key");



print("vote is temprering");
print("now you will hove to go again vote = ");


newbjp = 19;
newcongress = 21;
newothers = 20;
newtmc = 24;
newaap = 27;

newage = int(input("enter your age = "));
if(newage>=18):
    print("you are eligible");
    print("press b for bjp\npress c for congress\npress a for other\npress aap for aap\npress t for tmc");
    party = str(input());
    if(party == 'b'):
        print("you voted to bjp");
        newbjp = newbjp + 1;
        print("vote of bjp is ", newbjp);
    elif(party == 'c'):
        print("you voted to congress");
        newcongress = newcongress + 1;
        print("vote of congress is ", newcongress);
    elif(party == 'o'):
        print("you voted to others");
        newothers = newothers + 1;
        print("vote of others is ", newbjp);
    elif(party == 'b'):
        print("you voted to aap");
        newaap = newaap + 1;
        print("vote of b is ", newaap);
    elif(party == 't'):
        print("you voted to tmc");
        newtmc = newtmc + 1;
        print("vote of tmc is ", newtmc);



else:
    print("you are not eligible = ");



result = str(input("press y for know the result or n for not = "));
if(result == 'y'):
    print("bjp , tmc, other, aap, congress");
    print(newbjp,newtmc, newothers, newaap, newcongress);

else:
    print("you press wrong key");


















