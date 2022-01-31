"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

from typing import List, Tuple

def minmax(data: List) -> Tuple:

    _min, _max = data[0], data[0]
    for i in data:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

        return _min, _max


#test function
if __name__ == '__main__':
    print(minmax([1,2,4,5,-6,2,45]))