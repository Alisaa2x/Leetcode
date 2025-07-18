class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruit_count = {} 
        l = 0
        max_fruit = 0               

        for r in range(len(fruits)):
            fruit_count[fruits[r]] = fruit_count.get(fruits[r], 0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] < 1:
                    del fruit_count[fruits[l]]
                l += 1 
                
            max_fruit = max(max_fruit, r - l + 1) 
        
        return max_fruit
