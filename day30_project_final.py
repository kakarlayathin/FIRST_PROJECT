# ==========================================
# PROJECT: Data Auditor (Combines Days 1-29)
# ==========================================

def clean_and_sort(nums):
    seen = {}
    cleaned = []
    for num in nums:
        if num not in seen:
            seen[num] = True
            cleaned.append(num)

    for i in range(len(cleaned)):
        for j in range(i +1, len(cleaned)):
            if cleaned[i]>cleaned[j]:
                temp = cleaned[i]
                cleaned[i] = cleaned[j]
                cleaned[j] = temp
    return cleaned

def shift_by_one(nums):
    result = []
    for num in nums:
        result.append(num +1)
    return result

def find_single_duplicates(nums):
    x =0
    for num in nums:
        x = x ^num
    return x

def summary_range(nums):
    if not nums:
        return []
    result = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i - 1]))
            start = nums[i]


    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(str(start) + "->" + str(nums[-1]))

    return result
def missing_range(nums, lower, upper):
    result = []
    prev = lower - 1

    for num in nums:
        if num - prev > 1:
            if prev + 1 == num - 1:
                result.append(str(prev + 1))
            else:
                result.append(str(prev + 1) + "->" + str(num - 1))
        prev = num


    if upper - prev > 0:
        if prev + 1 == upper:
            result.append(str(prev + 1))
        else:
            result.append(str(prev + 1) + "->" + str(upper))
    return result

def is_valid_data(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching:
            if not stack:
                return False
            if stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left = left + 1
        else:
            right = right - 1
    return None


def max_subarray(nums):
    if not nums:
        return 0
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# ==========================================
# MAIN EXECUTION (This runs everything)
# ==========================================

raw_data = [4, 1, 2, 2, 8, 9, 15, 16, 17, 20]
data_string = "{ [1, 2, 3] }"
lower = 0
upper = 20
target = 10

# 1. Clean the data
cleaned = clean_and_sort(raw_data)
print("1. Cleaned & Sorted:", cleaned)

# 2. Find the unique duplicate using XOR
unique = find_single_duplicates(raw_data)
print("2. Number appearing once (XOR):", unique)

# 3. Shift all numbers by +1
shifted = shift_by_one(cleaned)
print("3. Shifted by +1:", shifted)

# 4. Group consecutive numbers
print("4. Summary Ranges:", summary_range(cleaned))

# 5. Find missing numbers
print("5. Missing Ranges:", missing_range(cleaned, lower, upper))

# 6. Validate the string brackets
print("6. Data string is valid?", is_valid_data(data_string))

# 7. Find a pair that adds up to target
pair = two_sum(cleaned, target)
if pair:
    print(f"7. Two numbers adding to {target}: {cleaned[pair[0]]} + {cleaned[pair[1]]} = {target}")
else:
    print(f"7. No pair found adding to {target}")

# 8. Find the maximum subarray sum
print("8. Maximum Subarray Sum:", max_subarray(cleaned))
