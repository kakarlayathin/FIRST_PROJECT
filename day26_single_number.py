print("===single_number===")
def single_number(numbers):
    result = 0
    for num in numbers:
        result = result ^ num
    return result

print(single_number([2, 2, 1]))        # Expected: 1
print(single_number([4, 1, 2, 1, 2]))  # Expected: 4
print(single_number([1]))              # Expected: 1
