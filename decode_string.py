def decoded_string(encoded_string):
    encoded_letters=encoded_string.split("0")

    decoded_string=""

    for letter in encoded_letters:
        position=len(letter)
        if position>0:
            decoded_string+=chr(position+ord("A")-1)
    return decoded_string    

encoded_string=input("Enter binary encoded msg:")
decoded_words=decoded_string(encoded_string)
print(decoded_words)