# !/usr/bin/python3


from typing import List

def checkSubarraySumBF(nums: List[int], k: int) -> bool:
    '''
    uses brute force to check if 
    there is a subarray of len > 1 where the sum is a multiple of k.
    T: O(n^2)
    S: O(1)
    '''
    if len(nums) < 2:
        return False
    for idx in range(len(nums)):
        summed = nums[idx]
        for jdx in range(idx, len(nums)):
            summed += nums[jdx]
            if summed % k == 0:
                return True
    return False
    
def checkSubarraySum(nums: List[int], k: int) -> bool:
    '''
    uses hash table (dict) and qualities of multiples to check if 
    there is a subarray of len > 1 where the sum is a multiple of k.
    The idea is that if we run into another modulo that is the same (not next to eachhoter)
    then we have added enough numbers to get mod 0
    T: O(n)
    S: O(n)
    accepted on https://leetcode.com/problems/continuous-subarray-sum/
    '''
    if len(nums) < 2:
        return False
    if set(nums) == {0}: # list of 0's, so always true
        return True
    if k == 0: # (not all 0's, so can't mod by 0)
        return False
        
    summed = nums[0] % k
    mod_dict = {summed:0}    
    for idx, num in enumerate(nums):
        if idx == 0: # hacky to get all proper indexes
            pass # skip the guy we got in there already
        summed += num
        summed %= k
        if summed in mod_dict and mod_dict[summed] != idx:  # if its there and not our index
            return True
        mod_dict[summed] = idx

    return False