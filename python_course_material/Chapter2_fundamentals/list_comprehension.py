numbers = [0,1,2,3,4,5]

double_numbers = [num * 2 for num in numbers]

print(double_numbers)

friend_ages = [21, 34, 25, 52]

print_age = [f"My friend's age is {age}" for age in friend_ages]

print(print_age)


list_friends = ["Rolf", "Anna", "Bob", "Eva"]
name = str(input("Enter name of a friend ? "))
list_lower_friend = [friend.lower() for friend in list_friends]

if name.lower() in list_lower_friend:
    print(f" {name.title()} is your friend")