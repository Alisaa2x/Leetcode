class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        inNums = set()
        ptr = 0

        for num in nums1:
            inNums.add(num)

        while ptr < len(nums2):
            if nums2[ptr] in inNums:
                res.append(nums2[ptr])
                inNums.remove(nums2[ptr])
            ptr += 1

        return res