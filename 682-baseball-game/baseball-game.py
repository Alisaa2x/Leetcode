class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []

        for char in operations:
            if char.isdigit() or (char.startswith('-') and char[1:].isdigit()): 
                record.append(int(char)) 
            if char == "C":
                record.pop()
            elif char == "D":
                record.append(record[-1] * 2)
            elif char == "+":
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])

        return sum(record)