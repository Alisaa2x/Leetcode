class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []
        i = n - 1

        while i >= 0:
            # skip spaces
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break

            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1

            res.append(s[j + 1:i + 1])
            i = j - 1

        return " ".join(res)