#!/usr/bin/python3

from itertools import combinations

from  typing import List


def combine(num: int, k: int) -> List[List[int]]:
    '''
    pretty shitty! but fast. whats the smarter way?
    Author: John Feilmeier
    '''
    return list(combinations(list(range(1,num+1)), k))

def combine_better(num: int, k: int) -> List[List[int]]:
    '''
    depth-first search to add all numbers to each babylist
    recursive methods found here https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
    similar to the C implemetnation
    '''
    pass