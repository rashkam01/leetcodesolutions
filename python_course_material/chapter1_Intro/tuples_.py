short_tuple = ("Rolf", "bob")

# The tuple is not getting modified but we are creating new tuple with same name 
short_tuple = short_tuple + ("Jen",) # , is to identify as a tuple and not a string 

print(short_tuple)