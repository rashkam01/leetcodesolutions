from math import sqrt
from statistics import mean

def standard_deviation(list1):
    if list1!= []:
        average = mean(list1)
        var = sum((i-average) ** 2 for i in list1) / (len(list1) - 1)
        standard_dev = sqrt(var)
        return standard_dev
    else:
        return "empty list"

print(standard_deviation([]))
