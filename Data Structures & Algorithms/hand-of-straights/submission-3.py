class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hashmap = {}
        if n % groupSize:
            return False
        
        """
        1, 1, 2, 2, 3, 4 -> False 2 groups



        """

        for i in hand:
            hashmap[i] = hashmap.get(i, 0) + 1

        unique = list(hashmap.keys())
        heapq.heapify(unique)
        for round in range(n//groupSize):
            minval = unique[0]
            for val in range(minval, minval+groupSize):
                if val not in hashmap:
                    return False
                hashmap[val] -= 1
                if hashmap[val] == 0:
                    if val != unique[0]:
                        return False
                    else:
                        heapq.heappop(unique)
        return True 





        """
        1,2,4,2,3,5,3,4
        1: 1
        2: 2
        3: 2
        4: 2
        5: 1

        1,2,3,3,4,5,6,7
        1:1
        2:1
        3:2
        4:1
        5:1
        6:1
        7:1
        """