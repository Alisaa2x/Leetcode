class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        ans = 0
        current = 0 
        prev = 0
        for i in range(1, len(s)):
                
            if s[i] == s[i - 1]:
                count += 1
                    
            else:
                prev = current
                current = count
                count = 1
                
                ans += min(prev, current)
            
        prev = current
        current = count
        ans += min(prev, current)
        
        return ans