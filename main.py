# def squares(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

def squares(nums):
    for i in nums:
        yield(i*i) # Yields on result at a time

#nums = squares([1,2,3,4,5])
#nums = [x*x for x in [1,2,3,4,5]] -> List Comprehension
nums = (x*x for x in [1,2,3,4,5]) # Round brackets = Generator object

print(nums)
print(list(nums))
# print(next(nums)) #1 - 1
# print(next(nums)) #2 - 4
# print(next(nums)) #3 - 9
# print(next(nums)) #4 - 16
# print(next(nums)) #5 - 25

for num in nums:
    print (num)