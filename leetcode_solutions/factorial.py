def factorial_calculator(n):
    factorial = 1
    for f in range(1, n+1):
        factorial = factorial* f 
    
    return factorial 


factorial_number = factorial_calculator(5)

print(factorial_number)