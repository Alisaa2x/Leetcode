class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        stack = []
        ans = []

        i = 0
        while i < len(word):
            stack.append(word[i])
            if word[i] == ch:
                while stack:
                    ans.append(stack.pop())
                i += 1
                while i < len(word):
                    ans.append(word[i])
                    i += 1
                return ''.join(ans)
            i += 1

        return word 