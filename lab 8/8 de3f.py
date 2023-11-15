def threeSum(nums, target):
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 2):
        a = nums[i]
        delta = 10 ** 10
        start = i + 1
        end = n - 1

        new_target = target - nums[i]

        while start < end:
            val = nums[start] + nums[end]

            if abs(delta) > abs(val - target):
                delta = target - val

            if val == new_target:
                return target
            elif val < new_target:
                start += 1
            else:
                end -= 1

        return target - delta


print(threeSum([-1, 0, 1, 2, -1, -4], 10))
