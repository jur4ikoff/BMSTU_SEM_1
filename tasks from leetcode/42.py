def trap(height: list[int]) -> int:
    n = len(height)
    res = 0
    for i in range(1, n - 1):
        max_left = height[i]
        for j in range(i):
            max_left = max(max_left, height[j])

        max_right = height[i]
        for j in range(i, n):
            max_right = max(max_right, height[j])

        res += min(max_left, max_right) - height[i]

    return res


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
