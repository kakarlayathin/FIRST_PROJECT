print("===missing_number_math===")
def missing_number_math(numbers):
    n = len(numbers)
    expected_sum = n* (n +1)//2
    actual_sum = 0


    for num in numbers:
        actual_sum = actual_sum + num
    return expected_sum - actual_sum

print(missing_number_math([3, 0, 1]))           # Expected: 2
print(missing_number_math([0, 1]))              # Expected: 2
print(missing_number_math([9,6,4,2,3,5,7,0,1]))