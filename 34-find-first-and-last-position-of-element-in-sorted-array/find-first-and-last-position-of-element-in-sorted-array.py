class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res

        # Find leftmost index
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if l < len(nums) and nums[l] == target:
            res[0] = l
        else:
            return res  # target not found at all

        # Find rightmost index
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        res[1] = r

        return res
# Time: O(2*log(n)) & Space: (1)