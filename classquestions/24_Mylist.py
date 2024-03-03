
import sys
Mylist = [1, 2, 3, 'abc', True, 3.14, 'null', 3 +4j]
print(Mylist);
print(type(Mylist));
print(sys.getsizeof(Mylist));
print(Mylist[3]);
print(Mylist[3][0:2]);
print(Mylist.append("hello"));