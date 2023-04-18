friends_ages = {"Rolf": 24, "Bob": 67, "Anne": 45}

print(friends_ages["Rolf"])

friends_ages["Bob"] = 20 

print(friends_ages)

list_to_dict = [("Rolf", 24), ("Bob", 67), ("Anne", 45)]
friends_list = [["Rolf", 24], ["Bob", 67], ["Anne", 45]]
friends = dict(list_to_dict)
friends_list_to_dict = dict(friends_list)

print(friends)
print(friends_list_to_dict)