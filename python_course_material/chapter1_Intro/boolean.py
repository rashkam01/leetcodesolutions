my_number = 5 
user_guess = int(input("Pick a number between 1 and 10: "))

matches = (user_guess == my_number)

print(f"You got it right: {matches}")