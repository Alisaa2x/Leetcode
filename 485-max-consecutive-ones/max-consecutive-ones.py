class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        most = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                most = max(most, count)
                count = 0

        return max(most, count)