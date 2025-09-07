class Solution:
    def isValidWindow(self, f_map):
        for key in f_map:
            if f_map[key] > 0:
                return False 
        return True 

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1

        l,r,minLen,res = 0,0,len(s),""
        while r < len(s):
            if s[r] in count:
                count[s[r]] -= 1
            
            while (not self.isValidWindow(count)) and r < len(s):
                r += 1

                if r < len(s) and s[r] in count:
                    count[s[r]] -= 1 
            
            curr_length = (r - l) + 1 
        
            if curr_length < minLen:
                minLen = curr_length 
                res = s[l:r+1]

            while(self.isValidWindow(count)) and l < len(s):
                curr_length = (r - l) + 1 
                
                if curr_length <= minLen: 
                    minLen = curr_length 
                    res = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1 
                l += 1
            r += 1 

        return res 