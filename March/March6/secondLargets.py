def secondLargest(nums):
    first = float('-inf')
    second = float('-inf')
    for num in nums:
        if (num > first):
            second = first
            first = num
        elif num > second and first < second:
            second = num
    return second


nums = [10, 5, 8, 20, 3]
second = secondLargest(nums)
print(second)