def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)+1):
        for j in range(0, i):
            if nums[i]+nums[j] == target:
                return [j, i]
    return [-1, -1]


def two_sum_optimized(nums, target):
    need_dict = {}
    ret = [-1, -1]
    size = len(nums)
    if size > 1:
        for i in range(size):
            if nums[i] in need_dict:
                ret = [need_dict[nums[i]], i]
            else:
                need_dict[target - nums[i]] = i
    return ret


if __name__ == '__main__':
    print(two_sum_optimized(nums=[2, 7, 11, 15], target=9))
