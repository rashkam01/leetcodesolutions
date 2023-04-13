def containsDuplicate(mylist = []) -> bool:
    temp1 = set(mylist)
    l2 = len(mylist)
    l1 = len(temp1)
    if (l1 != l2):
        return True
    else:
        return False

if __name__ == '__main__':

    a = [1,2,3,4,1]
    result = containsDuplicate(a)
    print(result)
