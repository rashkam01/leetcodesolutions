
def remove_duplicates(lst):
    no_duplicate_list = []
    for i in lst:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
    return no_duplicate_list

print(remove_duplicates([1,3,2,1,5,3,5,1,4]))