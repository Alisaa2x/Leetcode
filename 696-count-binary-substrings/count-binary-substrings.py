class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        group_len = []
        
        for i in range(1, len(s)):
            
            if s[i] == s[i - 1]:
                count += 1
                
            else:
                group_len.append(count)
                count = 1
        group_len.append(count)
        
        ans = 0 
        
        for i in range(1, len(group_len)):
            ans += min(group_len[i-1], group_len[i])
            
        
        return ans