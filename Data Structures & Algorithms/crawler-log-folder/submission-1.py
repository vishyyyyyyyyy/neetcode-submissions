class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            print(stack)
            if log == "../" and stack:
                stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        

        count = 0
        for log in stack:
            if log != "../" and log!="./":
                count +=1
        
        return count