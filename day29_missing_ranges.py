print("===missing_range===")
def missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1

    for num in nums:
        # Check if there is a gap between prev and num
        if num - prev > 1:
            if prev + 1 == num - 1:
                result.append(str(prev + 1))
            else:
                result.append(str(prev + 1) + "->" + str(num - 1))
        prev = num

    # Check the gap after the last number
    if upper - prev > 0:
        if prev + 1 == upper:
            result.append(str(prev + 1))
        else:
            result.append(str(prev + 1) + "->" + str(upper))

    return result

# === TEST CASES ===
print(missing_ranges([0, 1, 3, 50, 75], 0, 99))  # Expected: ['2', '4->49', '51->74', '76->99']
print(missing_ranges([], 1, 1))                   # Expected: ['1']
print(missing_ranges([-1], -1, -1))               # Expected: []