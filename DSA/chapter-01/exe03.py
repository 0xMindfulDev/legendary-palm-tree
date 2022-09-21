"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

from typing import List, Tuple

def minmax(data: List) -> Tuple:

    _min, _max = data[0], data[0]
    for num in data:
        if num < _min:
            _min = num
        if num > _max:
            _max = num

    return _min, _max


#test function
if __name__ == '__main__':
    print(minmax([1,2,4,5,-6,2,45]))
    print(minmax([1,2,3,4,5]))