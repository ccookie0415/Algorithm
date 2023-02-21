def backtrack_powerSet(nums):
    res = []

    def backtrack(start, path):
        res.append(path)

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])

    return res

print(backtrack_powerSet([1,2,3]))

# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

def backtrack_permute(nums):
    res = []

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])

        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()

    backtrack([])

    return res

print(backtrack_permute([1,2,3]))

# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]