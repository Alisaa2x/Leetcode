class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefixes = {0:1}
        current_sum = 0 
        result = 0
        
        for num in nums:
            current_sum += num
            diff = current_sum - goal 
            result += prefixes.get(diff, 0)
            prefixes[current_sum] = prefixes.get(current_sum, 0) + 1 
        
        return result