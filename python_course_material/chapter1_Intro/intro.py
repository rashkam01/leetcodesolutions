integer_division = 13 // 5

print(integer_division)

remainder = 10 % 5 
print("This is the remainder " + f"{remainder}")


friend_name = "Jose"
final_greeting = "How are you,{name}? "
jose_greeting = final_greeting.format(name=friend_name)

print(jose_greeting)

friend_name = "bob"
bob_greeting = final_greeting.format(name=friend_name)
print(bob_greeting)

my_name = "Rashmi"

your_name = input("Enter your name: ")

print(f"Hello, {your_name}, my name is {my_name}")