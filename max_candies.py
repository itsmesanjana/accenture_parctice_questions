def max_candies(n, prices, money):
    # Step 1: Separate free candies and paid candies
    paid_candies = []
    free_candies = 0
    
    for price in prices:
        if price % 5 == 0:
            free_candies += 1
        else:
            paid_candies.append(price)
    
    # Step 2: Sort paid candies in ascending order
    paid_candies.sort()
    
    # Step 3: Buy as many paid candies as possible
    candies_bought = 0
    
    for price in paid_candies:
        if money >= price:
            money -= price
            candies_bought += 1
        else:
            break
    
    # Step 4: Total candies Bob can get
    total_candies = candies_bought + free_candies
    
    return total_candies

# Example usage:
n = 6 #Available no of candies..
prices = [10, 2, 3,1,3, 5, 7]
money = 10

print(max_candies(n, prices, money))  # Output: 4 (Bob can buy the candies priced at 2, 3, 5 (free), 10 (free))
