class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'{':'}', '(':')', '[':']'}
        stack = []
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if len(stack) == 0 or char != hashmap[stack.pop()]:
                    return False
        return len(stack) == 0        