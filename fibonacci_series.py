def fibonacci_series(terms):
    n1 = 0
    n2 = 1
    
    # Print the first two terms
    print(n1)
    print(n2)
    
    # Loop to generate the rest of the series
    for i in range(2, terms):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum

# Call the function with the number of terms you want
fibonacci_series(7)
