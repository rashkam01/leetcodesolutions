list1 = [0,0,1,1,1,2,2,3,3,4]

large_integer = ""
for  val in list1:
    large_integer += str(val)

adding_one = str(int(large_integer) +1)

list2 = []

for i in range(len(adding_one)):
    num = adding_one[i]
    list2.append(int(num))

print(list2)


