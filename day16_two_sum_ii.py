print("===two_sum_ii===")
def two_sum(numbers , target):
    left = 0
    right = len(numbers) -1
    while left <right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left +1 , right +1]
        elif total < target:
            left = left+1
        else:
            right = right -1
    return []

print(two_sum([2, 7, 11, 15], 9))   # Expected: [1, 2]
print(two_sum([2, 3, 4], 6))        # Expected: [1, 3]
print(two_sum([-1, 0], -1))

