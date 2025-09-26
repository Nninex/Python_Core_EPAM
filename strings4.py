'''
Data Types. Strings. Task 4 
Write a function that checks whether a string is a palindrome or not. The usage of any reversing functions is prohibited.
'''
def check_str(s: str):
    
    res_str = ''
    for char in s:
        if not char.isalnum():
            continue
        res_str += char.lower()

    return res_str == res_str[::-1]
