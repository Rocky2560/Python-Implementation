
def count_frequency(arr):
    frequncy = {}
    for num in arr:
        if num in frequncy:
            frequncy[num] += 1
        else:
            frequncy[num] = 1
    return frequncy

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequecny_count = count_frequency(nums)
print(frequecny_count)