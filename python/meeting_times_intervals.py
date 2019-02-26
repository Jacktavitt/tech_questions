# !/usr/bin/python3

''' Given an array of meeting time intervals consisting of 
    start and end times [[s1,e1],[s2,e2],...] (si < ei), 
    find the minimum number of conference rooms required. 
    
    Author: John Feilmeier
        github.com/jacktavitt
    Source: Leetcode (1337code?)    
'''
INPUT1 = [[0, 30],[5, 10],[15, 20]]
# Output:2
INPUT2 = [[0, 10], [5, 25], [20, 30],[27, 28]]
# Output: 2

# The problem I ran into was, in the brute force attempt, counting the same room twice (in a nested loop, the overlap occurs for both)
# I thought, "maybe i can pop that value off after i've checked for room overlaps" BUT you can't do that when you're iterating in python

# The solution uses a heap to keep track of the rooms. THink of the rooms as buckets:
# one rooms can accommodate as many meetings as you want, as long as those times don't overlap.
# so we only really need to increment the number of required rooms when we need to put a meeting in an empty room.

# you could do this with a list, but it is simpler to use the heap implemented in python,
import heapq
# https://docs.python.org/3/library/heapq.html

def minimum_meeting_rooms(meeting_times):
    '''
    receiving an unsorted list of meeting times [[2, 5], [9, 13], [3, 7]]
    returns an integer representing how many different rooms we need
    '''
    if len(meeting_times) == 1:
        # there is only one meeting
        return 1
    # sort list by start times
    # this allows us to only need to check the end time of the previous meeting
    meeting_times.sort(key=lambda sched: sched[0])
    # initialize heap as empty list
    room_heap = []
    # stick the first meeting end time in there
    heapq.heappush(room_heap, meeting_times[0][1])
    # since we have a default meeting, set to 1 room
    num_rooms = 1
    # now iterate over meeting times, not counting first, already-pushed meeting end time
    for meeting in meeting_times[1:]:
        start, end = meeting[0], meeting[1]
        # if the start time is after the current meeting:
        if room_heap[0] <= start:
            # then we can use the room
            heapq.heappop(room_heap)
        else:
            # we need another room
            num_rooms += 1
        # stick this meeting on the room heap either way
        heapq.heappush(room_heap, end)
    
    return num_rooms

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # In [13]: print(minimum_meeting_rooms(INPUT1))                                   
    # 2
