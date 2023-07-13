# this time, let's use a list of tuples rather than a dict


def twoSum(nums):  # don't use camelCase except for class names -- try to use snake_case
    numMap = []  # variables should also be snake_case

    for index, one_number in enumerate(nums):
        numMap.append((one_number, index))
        print(numMap)


twoSum([1, 2, 3, 4, 5, 9])
