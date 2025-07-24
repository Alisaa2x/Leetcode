class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for op in tokens:
            if op.isdigit() or (op.startswith("-") and op[1:].isdigit()):
                stack.append(int(op))
            elif op == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif op == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif op == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif op == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
        return stack[-1]