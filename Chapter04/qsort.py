from time import sleep

def quicksort(array):
    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = array[0] # Recursive case
        # Sub-array of of all the elements less than the privot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of of all the elements greater than the privot
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

def print_items(List):
    for item in List:
        print(item)

def print_items2(List):
    for item in List:
        sleep(1)
        print(item)

if __name__ == "__main__":
    print(quicksort([10,5,2,3]))
    t = [2,4,6,8,10]
    print_items(t)
    print_items2(t)

