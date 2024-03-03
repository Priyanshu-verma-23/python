FirstNumber = int(input("enter your first number = "));
SecondNumber = int(input("enter your second number = "));
operation = str(input("enter your operation = "));


if(operation == '+'):
    result = FirstNumber + SecondNumber;
    print(result);
if(operation == '-'):
    result = FirstNumber - SecondNumber;
    print(result);
if(operation == '*'):
    result = FirstNumber * SecondNumber;
    print(result);
if(operation == '/'):
    result = FirstNumber / SecondNumber;
    print(result);
if(operation == '%'):
    result = FirstNumber % SecondNumber;
    print(result);
if(operation == '**'):
    result = FirstNumber ** SecondNumber;
    print(result);
if(operation == '//'):
    result = FirstNumber // SecondNumber;
    print(result);



