default_y = 3

def add(x, y = default_y):
    total = x + y 
    print(total)

add(2)

# modifying defalut value does not change 
default_y = 4
add(2)