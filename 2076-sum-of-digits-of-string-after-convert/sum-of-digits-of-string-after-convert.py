class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted_num_str = "".join([str(ord(char) - ord('a') + 1) for char in s])
        
        current_num = int(converted_num_str)
        
        for _ in range(k):
            digit_sum = 0
            for digit in str(current_num):
                digit_sum += int(digit)
            
            current_num = digit_sum

        return current_num