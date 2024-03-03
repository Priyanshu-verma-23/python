Fruit = ['apple', 'bannana','mango', 'orange']
num1 = [1, 2, 3, 4, 5];

Fruit.append(num1);
print(Fruit)

newlist = [];
newlist.append(Fruit[1]);
newlist.append(num1[1])

print(newlist)

Fruit[4].insert(4 ,newlist )
print(Fruit)