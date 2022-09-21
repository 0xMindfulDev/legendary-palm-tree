"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""


def solution(n: int) -> int:
    sum = 0
    for i in range(1,n):
        sum += i*i

    return sum



print(solution(5))  #30