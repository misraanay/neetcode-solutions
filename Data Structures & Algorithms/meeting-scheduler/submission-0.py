class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        s1, s2 = 0, 0
        while s1 < len(slots1) and s2 < len(slots2):
            a, b = slots1[s1], slots2[s2]

            if a[0] >= b[1]:
                s2+=1
                continue
            if b[0] >= a[1]:
                s1+=1
                continue

            if min(a[1], b[1]) - max(a[0], b[0]) >= duration:
                return [max(a[0], b[0]),  max(a[0], b[0]) + duration]
            
            if min(a[1], b[1]) == a[1]:
                s1 += 1
            else:
                s2 += 1

        return []

        