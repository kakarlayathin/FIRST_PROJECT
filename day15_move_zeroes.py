print("===MOVE ZEROES===")
def move_zeroes(numbers):
   result = []
   zero_count = 0
   for num in numbers:
       if num == 0:
           zero_count = zero_count + 1
       else:
           result.append(num)
   for i in range(zero_count):
       result.append(0)
   return result
print(move_zeroes([0, 1, 0, 3, 12]))   # Expected: [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))          # Expected: [1, 0, 0]
print(move_zeroes([1, 2, 3]))

