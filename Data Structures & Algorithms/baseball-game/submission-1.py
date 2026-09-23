class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]

        for i in range(len(operations)):
            if operations[i] == "+":
                if len(stack) >= 2 :
                    stack.append(stack[-1] + stack[-2])
            elif operations[i] == "D":
                if stack:
                    stack.append(stack[-1]*2)
            elif operations[i] =="C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)