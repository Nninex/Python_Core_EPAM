'''
OOP Basics. Task 4 
Implement a custom dictionary that will memorize the 5 latest changed keys. Using method “get_history” return these keys. 
Example: ```python  d = HistoryDict({“foo”: 42}) d.set_value(“bar”, 43) d.get_history() 
[“bar”] ``` 
'''
class HistoryDict:
    def __init__(self, data=None):
        self._data = dict(data) if data else {}
        self._history = []

    def set_value(self, key, value):
        self._data[key] = value
        self._history.append(key)
        if len(self._history) > 5:
            self._history.pop(0)

    def get_value(self, key):
        return self._data.get(key)

    def get_history(self):
        return list(self._history)

'''
from collections import deque

class HistoryDict:
    def __init__(self, data=None):
        self._data = dict(data) if data else {}
        self._history = deque(maxlen=5)

    def set_value(self, key, value):
        self._data[key] = value
        self._history.append(key)

    def get_value(self, key):
        return self._data.get(key)

    def get_history(self):
        return list(self._history)


'''
