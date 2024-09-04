def reverse_words_in_string(s):
    words=s.split()
    reversed_words=words[::-1]
    reversed_string=' '.join(reversed_words)
    return reversed_string

input_string=input("Enter a string: ")
result=reverse_words_in_string(input_string)
print("The string with reversed words is:",result)
