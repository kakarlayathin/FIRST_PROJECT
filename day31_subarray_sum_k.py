print("===subarray_sum_k===")
def subarray_sum(nums, k):
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum = current_sum + num
        if (current_sum -k) in prefix_sum_count:
            count = count + prefix_sum_count[current_sum -k]
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) +1
    return count

print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 2, 3], 3))
print(subarray_sum([1], 0))