class Solution:
    def expand(self, s: str) -> List[str]:

        n = len(s)
        i = 0

        res  = [""]

        while i < n:
            if s[i] == "{":
                chars = ""
                while i < n and s[i] != "}":
                    if s[i] not in  "{,":
                        chars += s[i]
                    i+=1
                chars
                replace = []
                for char in chars:
                    replace.extend([word + char for word in res])
                res = sorted(replace)
            else:
                replace = []
                replace.extend([word + s[i] for word in res])
                res = replace
            i += 1

        return res
        
            



        