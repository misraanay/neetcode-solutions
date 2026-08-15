class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_st = ""
        for st in strs:
            encoded_st += f"{len(st)}#{st}"
        return encoded_st

    def decode(self, s: str) -> List[str]:
        lst = []
        index = 0
        num_str = ""
        while index < len(s):
            if s[index] == "#":
                num = int(num_str)
                lst.append(s[index + 1: index + num + 1])
                index = index + num + 1
                num_str = ""
            else:
                num_str += s[index]
                index += 1
        return lst
