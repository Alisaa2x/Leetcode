class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for letter in magazine:
            count[letter] = count.get(letter, 0) + 1

        for letter in ransomNote:
            if letter not in count or count[letter] == 0:
                return False
            else:
                count[letter] -= 1

        return True