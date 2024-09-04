def swap_charcters(input_string,ch1,ch2):
    swapped_string=''.join([ch2 if char==ch1 else ch1 if char==ch2 else char for char in input_string])
    return swapped_string

input_string =input("Enter input String:")
ch1 = input("Enter first chacter that u want to swap from above input string : ")
ch2 = input("Enter second chacter that u want to swap from above input string :")
# result = swap_characters(input_string, ch1, ch2)
result=swap_charcters(input_string,ch1,ch2)
print(result)