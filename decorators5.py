'''
Functions. Decorators. Final Task 1. 
Implement a function that works the same as str.split method (without using str.split itself, ofcourse). Pay attention to strings with multiple
spaces. For example: ‘ Hi Python world!’ 
Example: ```python def split(data: str, sep=None, maxsplit=-1):
'''
from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here   
    """
    if data == '':
        return []

    # if maxsplit == 0 → no split, return whole string
    if maxsplit == 0:
        return [data.strip()] if sep is None else [data]

    result = []
    buffer = ""
    splits_done = 0

    i = 0
    n = len(data)

    if sep is None:
        # whitespace splitting
        while i < n:
            if data[i].isspace():
                if buffer:
                    result.append(buffer)
                    buffer = ""
                    splits_done += 1
                    if 0 < maxsplit == splits_done:
                        # consume rest
                        while i < n:
                            buffer += data[i]
                            i += 1
                        buffer = buffer.strip()
                        if buffer:
                            result.append(buffer)
                        return result
                # skip consecutive spaces
                while i < n and data[i].isspace():
                    i += 1
            else:
                buffer += data[i]
                i += 1
        if buffer:
            result.append(buffer)
        return result

    else:
        # fixed separator
        sep_len = len(sep)
        while i < n:
            if data.startswith(sep, i) and (maxsplit < 0 or splits_done < maxsplit):
                result.append(buffer)
                buffer = ""
                i += sep_len
                splits_done += 1
            else:
                buffer += data[i]
                i += 1
        result.append(buffer)
        return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
