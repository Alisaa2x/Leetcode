class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []

        for char in operations:
            if char == "C":
                record.pop()
            elif char == "D":
                record.append(record[-1] * 2)
            elif char == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(char)) 

        return sum(record)