a = 5   #0101
b = 6

print(format(a, 'b'))
print(format(b,'b'))
c = a ^ b
print('a', a) 
print('b', b) 
print('a ^ b = ',c)
print(format(c, 'b'))
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

matrix = [[112,42,83,119], \
               [56,125,56,49], \
               [15,78,101,43], \
               [62,98,114,108]]
print(matrix)