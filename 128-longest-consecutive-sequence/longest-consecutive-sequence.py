class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove dupes
        num1 = set(nums)
        # track max seq
        count = 0

        # loop through array
        for n in num1:
            # check if it the first element of the sequence
            if n - 1 not in num1:
                length = 0
                # find consecutive elements
                while n + length in num1:
                    length += 1
                count = max(count, length)
        return count