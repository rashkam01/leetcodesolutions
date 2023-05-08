def climbing_stairs(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
        
    for i in range(2,(n+1)):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]
    
number_of_step = climbing_stairs(1)

print(number_of_step)
    
    