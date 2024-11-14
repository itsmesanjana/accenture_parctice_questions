def climbstairs(n):
    if n==1:
        return 1
    
    dp1,dp2=1,1
    
    for i in range(2,n+1):
        current=dp1+dp2
        dp1,dp2=dp2,current
        
        return dp2

print(climbstairs(4))