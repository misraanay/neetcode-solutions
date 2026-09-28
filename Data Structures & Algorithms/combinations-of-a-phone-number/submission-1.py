class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
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

        def recurse(i, prefix):
            if i == len(digits):
                res.append(prefix)
                return
            else:
                for c in hmap[digits[i]]:
                    recurse(i+1, prefix + c)
            
        if digits:
            recurse(0, "")
        return res


