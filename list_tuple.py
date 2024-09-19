friends = ["apple", 3.44, "hari", False] #Unlike strigs, list are mutable
friends[0] = "grapes"
print (friends[2])
friends.append("neshan")    
print(friends)
li =[1,23,4,5,100]
# li.sort()
# li.reverse()
# li.insert(3,333)
# value = li.pop(3)
# print(value)
li.remove(23)
print(li)


# tuple
a = (1, 2, 3333, "ram")
print(type(a))
print(a[0])
no = a.count(2)
print(no)
print(a+(1,2))
print(a*2)
print(len(a))