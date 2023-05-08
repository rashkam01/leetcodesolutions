def mean(list1):
    add_number = 0
    if  list1 !=[]:
        for i in range(len(list1)):
            add_number += list1[i]
        return add_number/len(list1)
    else:
        return "empty list"


number = mean([4, 36, 45, 50,75])
print(number)

number = mean([])
print(number)



