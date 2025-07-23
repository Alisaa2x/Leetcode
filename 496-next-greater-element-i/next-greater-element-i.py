class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = [-1] * len(nums1) 

        for i in range(len(nums1)):
            #find where the occurrence of the number we are looking for starts 
            l = 0  

            while l < len(nums2) and nums2[l] != nums1[i]:
                l += 1 

            #l = 2 
            while l < len(nums2) and nums2[l] <= nums1[i]:
                l += 1
                
                if l < len(nums2) and nums2[l] > nums1[i]: 
                    output[i] = nums2[l]
                    break
                
        return output