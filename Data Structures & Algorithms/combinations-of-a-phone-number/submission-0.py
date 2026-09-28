class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def combination(prefix:str) -> List[str]:
            idx = len(prefix)
            if idx == len(digits):
                return [prefix]
            res = []
            for char in hmap[digits[idx]]:
                for ans in combination(prefix + char):
                    res.append(ans)
            return res
        return combination("")