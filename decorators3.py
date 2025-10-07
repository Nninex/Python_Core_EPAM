'''
Functions. Decorators. Decorators. Task 3. 
Create decorator validate which validates arguments in set_pixel function. All function parameters should be between 0(int) and 256(int) inclusive. 
In case if all parameters are valid, set_pixel function should return “Pixel created!” message. Otherwise, it should return “Function call is not valid!”
message. 
Use functools.wraps where is it necessary. 
Don’t forget about doc stings. 
Examples ```python  set_pixel(0, 127, 300) Function call is not valid! set_pixel(0,127,250) Pixel created! ``
'''
from functools import wraps

def validate(f):
  '''
  Decorator that validates all integer arguments of a function
  '''

  @wraps(f)
  def wrapper(*args, **kwargs):
      # validate positional args
      for arg in args:
          if not (isinstance(arg, int) and 0 <= arg <= 256):
              return "Function call is not valid!"
      # validate keyword args
      for arg in kwargs.values():
          if not (isinstance(arg, int) and 0 <= arg <= 256):
              return "Function call is not valid!"
      return f(*args, **kwargs)
  return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  ''' validate the pixels '''
  return "Pixel created!"
