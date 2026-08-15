class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs: #O(m)
            anagram_list = [0] * 26
            for letter in str: #O(n)
                anagram_list[ord(letter) - ord('a')] += 1
            anagram_tuple = tuple(anagram_list)
            if anagram_tuple in map:
                map[anagram_tuple].append(str)
            else:
                map[anagram_tuple] = [str]
        return list(map.values())
        