#!/usr/bin/python3

from  typing import List

def bitCount(num):
    '''
    shift bits a la https://wiki.python.org/moin/BitManipulation
    count the bits in a number
    '''
    count = 0
    while(num):
        num &= num -1
        count += 1
    return count

def readBinaryWatch(num: int) -> List[str]:
    '''
    four top lights are hours (0-11)
    six bottom are minutes (0-59)
    figure out all possible times, and return a list of those who's
    bit count is the same as our target number
    T: O(1) (really 720 but that is still constant)
    S: O(1) same as above, limited loop but hours and minutes

    this answer accepted by leetcode

    '''
    times_list = []
    for hour in range(12):
        for minute in range(60):
            if bitCount(hour) + bitCount(minute) == num:
                times_list.append(f"{hour}:{minute:02d}")
    return times_list

        