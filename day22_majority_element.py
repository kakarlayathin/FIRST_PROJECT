print("===majority_element===")
def majority_element(numbers):
    candidate = None
    count = 0
    for num in numbers:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count = count + 1
        else:
            count = count -1
    return candidate


print(majority_element([3, 2, 3]))                 # Expected: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))     # Expected: 2
print(majority_element([1]))                       # Expected: 1
