"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""


def is_even(k: int) -> bool:
    """
    function to determin if a given integer k is even
    """
    even = True
    for i in range(1,k+1):
        if even:
            even = False
        else:
            even = True


    return even

#using bitwise operator
def is_even2(k: int) -> bool:
    """
    takes advantage of the fact that the last bit of an
    even number is always 0.
    """
    # return not (k & 1)
    return (k & 1) == 0 #more readable

# test code
if __name__ == '__main__':
    print(is_even(20))
    print(is_even(11))

    print(is_even2(20))
    print(is_even2(11))