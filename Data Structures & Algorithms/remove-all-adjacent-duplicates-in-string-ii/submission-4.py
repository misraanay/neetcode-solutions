class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for i, char in enumerate(s):
            
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if  stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append([char, 1])


        st = ""
        for char, count in stack:
            st += char * count

        return st
