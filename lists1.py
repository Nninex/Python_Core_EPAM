'''
Data Types. Lists. Task 1 
Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form. 
Examples: 
Input: python ('red', 'white', 'black', 'red', 'green', 'black') Output: python ['black', 'green', 'red', 'white']
'''

from typing import List, Tuple

def sort_unique_elements(str_list: List[str]) -> List[str]:
    
    result = []
    for i in str_list:
        if i not in result:
            result.append(i)
    result.sort()
    return result

print(sort_unique_elements(['red', 'white', 'black', 'red', 'green', 'black']))
