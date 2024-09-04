def toss_and_score(S):
    score=0
    consecutive_heads=0
    
    for char in S:
        if char=="H":
            score+=2
            consecutive_heads+=consecutive_heads
            if consecutive_heads==3:
                break
        else:
            score-=1
            consecutive_heads=0
    return score

S=input("Enter string : ")
print(toss_and_score(S))