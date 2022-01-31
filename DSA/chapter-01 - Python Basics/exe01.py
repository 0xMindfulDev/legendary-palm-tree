"""Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""



def is_multiple(n: int, m: int) -> bool:
    """
    function to determine of n is a multiple of m
    """
    return n % m == 0


#test function
if __name__ == '__main__':
    print(is_multiple(20, 3)) #False
    print(is_multiple(21, 3)) #True
    print(is_multiple(77, 7)) #True