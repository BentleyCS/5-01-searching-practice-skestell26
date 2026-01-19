
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    pass
import random

def randomSearch(items: list, target) -> int:
    tries = 0

    while True:
        index = random.randrange(len(items))
        tries += 1

        if items[index] == target:
            print(f"Found target after {tries} tries")
            return index
def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    pass
def linearSearch(items: list, target) -> tuple[int, int]:
    checks = 0

    for index, value in enumerate(items):
        checks += 1
        if value == target:
            return index, checks

    return -1, checks

def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    pass
def binarySearch(items: list, target) -> tuple[int, int]:
    left = 0
    right = len(items) - 1
    checks = 0

    while left <= right:
        mid = (left + right) // 2
        checks += 1

        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, checks