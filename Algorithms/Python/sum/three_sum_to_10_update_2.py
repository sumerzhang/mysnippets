def three_sum(nums, target):
    nums.sort()
    n = len(nums)
    results = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return results

# 测试代码
nums = [3, 1, 4, 2, 2, 2, 9, 5, 7, 6, 1]
target = 10
result = three_sum(nums, target)
if result:
    print(f"找到了如下和为 {target} 的三个数的组合：")
    for r in result:
        print(r)
else:
    print(f"没有找到和为 {target} 的三个数")
