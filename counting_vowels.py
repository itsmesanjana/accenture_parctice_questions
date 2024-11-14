def count_vowels_in_substrings(s):
    vowels = set('aeiou')
    total_vowels = 0
    
    # Loop through all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            total_vowels += sum(1 for char in substring if char in vowels)
    
    return total_vowels

# Test the function
input_string = "ltcd"
result = count_vowels_in_substrings(input_string)
print(f"Total sum of vowels in substrings: {result}")
