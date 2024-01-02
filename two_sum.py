from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for number1, value1 in enumerate(nums):
            for number2, value2 in enumerate(nums):
                if number1 != number2 and value1 + value2 == target:
                    return [number1, number2]


#is accepted, but is slow and goes against o(n^2)

#above is accepted by leetcode without test under this line
nums = [2,7,11,15]
target = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6


solution = Solution()

solution.twoSum(nums, target)
solution.twoSum(nums2, target2)
solution.twoSum(nums3, target3)