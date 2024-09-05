def count_occurrences(S,N,C):
    return S.count(C)
S=input("")
N=int(input("Enter the len of strings:"))
C=input("Enter charcter to count:")
print(count_occurrences(S,N,C))