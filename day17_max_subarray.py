print("===max_subarray===")
def max_subarray(numbers):
    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for i in range(1, len(numbers)):
        num = numbers[i]
        current_sum = max(num, current_sum + num)
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
print(max_subarray([1]))                               # Expected: 1
print(max_subarray([5, 4, -1, 7, 8]))                  # Expected: 23