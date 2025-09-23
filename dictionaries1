'''
  Data Types. Dictionaries. Task 1. 
Write a Python program to count the frequency of each character in a string (ignore the case of letters). 
Example: 
Input: 'Oh, it is python' 
Output: {" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1
  '''

from typing import Dict
from collections import defaultdict

def get_dict(s: str) -> Dict[str, int]:
    freq = defaultdict(int)
    for char in s.lower():
        freq[char] += 1
    return dict(freq)

print(get_dict('Oh, it is python'))
