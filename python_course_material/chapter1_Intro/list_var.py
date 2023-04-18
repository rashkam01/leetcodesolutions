# list is mutable, it can be list or list of lists 

friends = [["Rolf", 24], ["Bob", 67], ["Anne", 45]]
friends.append( ["Jen", 54])
friends.remove(["Jen", 54])

print(friends)  # prints list
print(friends[0]) # prints 0th element of list ["Rolf", 24]
print(friends[0][0]) # prints 0th element of the 0th position in list "Rolf"