def twoSum(nums):
    numMap = {}
    n = len(nums)

    # for i in range(n):
    #     numMap[nums[i]] = i 
    #     print(numMap)

    for index, one_number in enumerate(nums):
        numMap[one_number] = index
        print(numMap)

twoSum([1,2,3,4,5,9])        