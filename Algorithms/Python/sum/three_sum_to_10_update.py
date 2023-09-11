#如果你想要进一步优化空间复杂度，可以考虑以下两个方面：
# 1. 不使用额外的数据结构： 你可以避免使用额外的数据结构来存储结果。
# 相反，你可以在找到一个符合条件的组合后，立即处理它，
# 而不是将它们全部存储在结果列表中。这可以减少内存占用。
# 2. 去除重复元素： 如果输入数组可能包含重复的元素，
# 你可以在算法中添加去重逻辑，以避免重复计算相同的组合。这可以减少不必要的运算。
def three_sum_to_10(nums):
    # 首先对数组进行排序
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # 去除重复元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 10:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # 去除重复元素
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 10:
                left += 1
            else:
                right -= 1

    return result

# 示例输入
nums = [1, 2, 2,  3, 4, 5, 6, 7, 8, 9]
result = three_sum_to_10(nums)
print(result)
