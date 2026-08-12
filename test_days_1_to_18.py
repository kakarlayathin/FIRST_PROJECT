print("==Q1: Move Zeroes (Day 15): "
      "Write a function move_zeroes(nums) that moves all 0s to the end.")
def move_zeros(numbers):
   result = []
   zero_count = 0
   for num in numbers:
       if num == 0:
           zero_count = zero_count + 1
       else:
           result.append(num)
   for i in range(zero_count):
       result.append(0)
   return result
print(move_zeros ([0, 1, 0, 3, 12]))


print(" Two Sum II (Two Pointer - Day 16): "
      "Write a function two_sum_sorted(numbers, target) that finds two numbers in a sorted array using the left/right pointer technique.")

def two_sum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left<right:
        total = numbers[left]+numbers[right]
        if total == target:
            return [left+1, right+1]
        elif total <target:
            left = left+1
        else:
            right = right -1
    return []

print(two_sum([2, 7, 11, 15],9))


print(" Maximum Subarray (Kadane's Algorithm - Day 17): "
      "Write a function max_subarray(nums) that finds the largest sum of a continuous subarray.")

def max_sum(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]
    for i in range(1, len(numbers)):
        num = numbers[i]
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4] ))


print(" Remove Duplicates (Day 9): "
      "Write a function remove_duplicates(nums) that returns a new list with only unique numbers.")
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
             result.append(num)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
