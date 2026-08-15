print("====review====")
print("==plus_one==")
def plus_one(digits):
    i = len(digits)-1
    while i >=0:
        if digits[i] < 9:
            digits[i] = digits[i] +1
            return digits
        else:
            digits[i] = 0
            i = i-1
    return [1] + digits

print(plus_one([1, 3, 3]))   # Expected: [1, 3, 4]
print(plus_one([4, 3, 2, 4])) # Expected: [4, 3, 2, 5]
print(plus_one([9, 9, 9, 9]))         # Expected: [1, 0, 0, 0, 0]

print("==two sum==")
def two_sum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left+1, right+1]
        elif total < target:
            left = left +1
        else:
            right = right -1
    return total

print(two_sum([2, 7, 11, 15], 9))   # Expected: [1, 2]
print(two_sum([2, 3, 4], 6))        # Expected: [1, 3]
print(two_sum([-1, 0], -1))