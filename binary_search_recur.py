def binary_search(list, low, high, item):
    if low > high:
        return None
    mid = (low+high)/2
    guess = list[mid]
    if guess == item:
        return mid
    if guess > item:
        low = 0
        high = mid -1
    else:
        low = mid + 1
        high = len(list)
    return binary_search(list,low,high,item)

