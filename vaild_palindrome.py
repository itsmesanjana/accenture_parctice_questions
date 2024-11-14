def isPalindrome(s):
    normalized_str=''.join(char.lower() for char in s if char.isalnum())

    reverse_arr=normalized_str[::-1]
    
    if reverse_arr==normalized_str:
        return True
    else:
        return False


print(isPalindrome("anj,na"))
    
    