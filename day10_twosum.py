def find_twosum(nums, target):
   for i in range (len(nums)):
        for j in range(i+1 ,len(nums)):
            if nums[i]+ nums[j] == target:
              return [i ,j]
result =find_twosum([2, 7, 11, 15], 9)
result1 = find_twosum([3, 2, 4], 6),
result2 = find_twosum([3, 3], 6)
print("For [2, 7, 11, 15], target 9, indices are:", result)
print("for [3, 2, 4], targrt 6, indicates are:", result1)
print("for [3, 3], targrt 6, indicates are:", result2)

print("===problem 2===")
def remove_duplicates(numbers):
    result3 = []
    for num in numbers:
        if num in result3:
            return True
        result3.append(num)
    return False

print(remove_duplicates([1, 2, 3, 1]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 1, 1, 1]))