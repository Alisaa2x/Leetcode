class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}

        for idx, num in enumerate(nums):
            pair = target - num
            if pair in lst:
                return [lst[pair], idx]
            lst[num] = idx
