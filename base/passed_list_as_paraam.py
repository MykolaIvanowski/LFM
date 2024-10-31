def addToList(val, list=[]):
 list.append(val)
 return list

list1 = addToList(1)
list2 = addToList(123,[])
list3 = addToList('a')
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

# list1 = [1,’a’]
# list2 = [123]
# lilst3 = [1,’a’]

print(list1 is list2) # False
print(list1 is list3) # True
