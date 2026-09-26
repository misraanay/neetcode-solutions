class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxPossible = len(min(strs, key=lambda x: len(x)))

        for i in range(maxPossible):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return s[:i]
        return strs[0][:maxPossible]
