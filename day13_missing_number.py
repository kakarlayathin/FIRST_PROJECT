print("===PROBLEM: FIND THE MISSING NUMBER===")
def find_missing(numbers):
    n = len(numbers)
    all_number = list(range(n +1))
    for num in all_number:
        if num not in numbers:
            return num
print(find_missing([3, 0, 1]))          # Expected: 2
print(find_missing([0, 1]))             # Expected: 2
print(find_missing([9,6,4,2,3,5,7,0,1])) # Expected: 8
