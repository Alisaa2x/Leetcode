class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}

        output = [-1] * len(nums1) 
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        for i in range(len(nums1)): 
            if nums1[i] in next_greater: 
                output[i] = next_greater[nums1[i]]

        return output 