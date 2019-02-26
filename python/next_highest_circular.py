# !usr/bin/python3

from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    '''
    brute force solution.
    go around until we hit the number or we hit a higher number.
    Author: John Feilmeier
    '''
    next_high = []
    for idx, n in enumerate(nums):
        searcher = idx
        good = True
        hn = -1
        while good == True:
            searcher += 1
            if searcher == len(nums):
                searcher = 0
            if searcher == idx:
                good = False
                break
            if nums[searcher] > n:
                hn = nums[searcher]
                break
        next_high.append(hn)
    return next_high