'''
Data Types. Strings. Task 1 
Fractions 
Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these
fractions and the sum result. 
For example: ```python 
a_b = ‘1/3’ c_b = ‘5/3’ get_fractions(a_b, c_b) ‘1/3 + 5/3 = 6/3’ ``
'''

def get_fractions(a_b: str, c_b: str) -> str:
    nums = a_b.split("/")
    print(nums)
    a, b = int(nums[0]), int(nums[1])
    nums2 = c_b.split("/")
    c = int(nums2[0])
    ac = a + c
    return  f'{a_b} + {c_b} = {ac}/{b}'
