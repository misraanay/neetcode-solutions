class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        filtered = []
        for triple in triplets:
            a, b, c = triple
            if a > x or b > y or c > z:
                continue
            filtered.append(triple)
        if not filtered:
            return False
        return [max(triple[0] for triple in filtered), max(triple[1] for triple in filtered),       max(triple[2] for triple in filtered)] == target