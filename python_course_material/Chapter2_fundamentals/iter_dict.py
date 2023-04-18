friends_age = {"Rolf": 25, "Anne": 23, "Bob": 35}

# printing the dictionary keys 
for name in friends_age:
    print(f"The key in the dictionary is {name}")


#printing values in dictionary items 
for age in friends_age.values():
    print(f"The age is {age}")


# name, age is descructuring the dict 
for name, age in friends_age.items():
    print(f"Hello, friend {name}, your age is {age}")
