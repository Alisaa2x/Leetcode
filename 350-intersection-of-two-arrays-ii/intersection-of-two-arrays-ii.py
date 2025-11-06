class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        res = []

        for n in nums1:
            count[n] = count.get(n, 0) + 1

        for n in nums2:
            if n in count and count[n] != 0:
                res.append(n)
                count[n] -= 1

        return res