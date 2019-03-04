# !/usr/env/python3

def list_recursive_merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    middle = int(len(unsorted)/2)
    left = recursive_merge_sort(unsorted[:middle])
    right = recursive_merge_sort(unsorted[middle:])

    return list_merge(left, right)


def list_merge(left, right):
    if not left or not right:
        return left or right
    result = []
    lidx = 0
    ridx = 0
    while len(result) < (len(left) + len(right)):
        if left[lidx] < right[ridx]:
            result.append(left[lidx])
            lidx += 1
        else:
            result.append(right[ridx])
            ridx += 1
        if lidx = len(left) or ridx = len(right):
            result.extend(left[lidx:] or right[ridx:])
            break

    return result


    
