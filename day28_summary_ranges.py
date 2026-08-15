print("===summary_range===")
def summary_ranges(nums):
    if not nums:
        return []

    result = []
    start = nums[0]

    for i in range(1, len(nums)):
        # If the current number is NOT exactly +1 of the previous one...
        if nums[i] != nums[i - 1] + 1:
            # The current range ends at nums[i - 1]
            if start == nums[i - 1]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i - 1]))
            # Start a new range from the current number
            start = nums[i]

    # After the loop, close the final range
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(str(start) + "->" + str(nums[-1]))

    return result

# === TEST CASES ===
print(summary_ranges([0, 1, 2, 4, 5, 7]))      # Expected: ['0->2', '4->5', '7']
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))  # Expected: ['0', '2->4', '6', '8->9']
print(summary_ranges([1]))                    # Expected: ['1'])