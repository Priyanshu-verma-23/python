groceries=['rice', 'wheat', 'maize', 'pulses', 'quinoa', 'curd', 'biscuits', 'chips', 'beans', 'bananas']
groceriesprice=[100, 150, 180, 50, 90, 200, 20, 100, 10, 30]
newlist = []
newlistprice = [];

print("welcome to in shop : ");
print("Note: Press the position of the object:");
print(groceries);
print(groceriesprice);

num1= int(input("Buy your 1st product = "));
objectnum = num1 - 1;
item1 = groceries[objectnum];
price = groceriesprice[objectnum];
newlist.append(item1);
newlistprice.append(price);


num2= int(input("Buy your 2nd Product = "));
objectnum = num2 - 1;
item2 = groceries[objectnum];
price = groceriesprice[objectnum];
newlist.append(item2);
newlistprice.append(price);


print("you can buy only maximum 2 item in a shop");
print("welcome to 2nd shop")

clothes=['skinny jeans', 't-shirts', 'shirts', 'trousers', 'baggy jeans', 'gown', 'frock', 'bodycon dress', 'lehenga','indo-western']
clothesprice=[500, 300, 800, 1000, 600, 2000, 700, 900, 5000, 2500]

print(clothes);
print(clothesprice);

num3= int(input("Buy your 3rd product = "));
objectnum = num3 - 1;
item3 = clothes[objectnum];
price = clothesprice[objectnum];
newlist.append(item3);
newlistprice.append(price);


num4= int(input("Buy your 4rd product = "));
objectnum = num4 - 1;
item4 = clothes[objectnum];
price = clothesprice[objectnum];
newlist.append(item4);
newlistprice.append(price);

jewelry=['earrings', 'ring', 'bracelet', 'anklet', 'earcuffs', 'toe ring', 'hair acessories', 'scruncies', 'floral-set', 'necklace']
jewelryprice=[200, 150, 400, 250, 300, 500, 450, 100, 350, 550]

print(jewelry);
print(jewelryprice);

num5= int(input("Buy your 5rd product = "));
objectnum = num5 - 1;
item5 = jewelry[objectnum];
price = jewelryprice[objectnum];
newlist.append(item5);
newlistprice.append(price);


num6= int(input("Buy your 6rd product = "));
objectnum = num6 - 1;
item6 = jewelry[objectnum];
price = jewelryprice[objectnum];
newlist.append(item6);
newlistprice.append(price);

footwear=['shoes', 'sandals', 'open-toe', 'flats', 'bellies', 'sneakers', 'tennis shoes', 'stilletoes', 'block heels', 'basketball shoes']
footwearprice=[2000, 3000, 2500, 4000, 1000, 1500, 3500, 1200, 2700, 4500]

print(footwear);
print(footwearprice);

num7= int(input("Buy your 7 product = "));
objectnum = num7 - 1;
item7 = footwear[objectnum];
price = footwearprice[objectnum];
newlist.append(item7);
newlistprice.append(price);


num8= int(input("Buy your 8 product = "));
objectnum = num8 - 1;
item8 = footwear[objectnum];
price = footwearprice[objectnum];
newlist.append(item8);
newlistprice.append(price);

food=['momos', 'fries', 'burger', 'pizza', 'sandwich', 'noodles', 'fried rice', 'manchurian', 'coffee', 'tea']
foodprice=[100, 150, 200, 400, 120, 250, 250, 300, 50, 20]

print(food);
print(foodprice);

num9= int(input("Buy your 9 product = "));
objectnum = num9 - 1;
item9 = food[objectnum];
price = foodprice[objectnum];
newlist.append(item9);
newlistprice.append(price);


num10= int(input("Buy your 10 product = "));
objectnum = num10 - 1;
item10 = food[objectnum];
price = foodprice[objectnum];
newlist.append(item10);
newlistprice.append(price);


print("your product list is = ", newlist);
print("and price of each product is = ", newlistprice);

Total = sum(newlistprice);
print("Total = ", Total);




