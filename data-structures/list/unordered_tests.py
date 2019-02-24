from unordered_list import UnorderedList

mylist = UnorderedList()

mylist.add(20)
mylist.add(40)
mylist.insert(1, 55)
mylist.insert(-2, 65)
print(mylist.index(65))
mylist.append(100)
print(mylist.index(100))