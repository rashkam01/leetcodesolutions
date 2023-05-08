def count_numbers(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] +=  + 1
        else:
            count_dict[i] = 1
    return count_dict

print(count_numbers([1,3,2,1,5,3,5,1,4]))