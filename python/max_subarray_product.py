from typing import List

def maxProduct(nums: List[int]) -> int:
    '''
    from https://www.geeksforgeeks.org/maximum-product-subarray-added-negative-product-case/
    then by me, John Feilmeier

    when going through a list, and lloking for a 'continuuous' thing,
    all we ever really care about is the value at idx, and the max or min gloablly.
    T: O(n)
    S: O(1)
    '''
    # answer can be negative, so minval
    ans = -float('inf')
    maxsofar = 1
    minsofar = 1
    for num in nums:
        if num > 0:
            # if positive, max gets bigger, min possibly gets smaller
            maxsofar *= num
            minsofar = min(1, minsofar*num)
        elif num == 0:
            # reset, but keep max as 0 as it may be answer
            maxsofar = 0
            minsofar = 1
        else:
            # number is negative
            temp = maxsofar
            # store max
            maxsofar = minsofar * num
            # if minsofar is negative, new max will be large
            minsofar = temp * num
            # new low for min
        # max will never ge to here as '1' unless '1' is the max.
        ans = max(ans, maxsofar)
        # bookeeping for situation where max is 0.
        if maxsofar <= 0:
            maxsofar = 1
            
    return ans
        