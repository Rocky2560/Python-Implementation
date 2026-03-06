def remove_duplicates(nums):
    uniqueNums = []
    for num in nums:
        if num not in uniqueNums:
            uniqueNums.append(num)
    return uniqueNums

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)