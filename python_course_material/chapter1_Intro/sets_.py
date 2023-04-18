art_friends = {"Rolf", "Anne", "Jen" } # sets cannot have duplicates and makes them a bad choice for duplicate items 
science_friends = {"Jen", "Charlie"} 

art_no_science = art_friends.difference(science_friends)
science_no_art = science_friends.difference(art_friends)
print(f"These friends are in art but not in Science {art_no_science}")
print(f"These friends are in science but not in art {science_no_art}")


not_in_both = art_friends.symmetric_difference(science_friends)
print(f"These friends are in either art or Science but not in both {not_in_both}")

in_both = art_friends.intersection(science_friends)
print(f"These friends are in both art and science {in_both}")

all_friends = art_friends.union(science_friends)
print(f"These are all friends {all_friends}")     # common elements not repeated 
