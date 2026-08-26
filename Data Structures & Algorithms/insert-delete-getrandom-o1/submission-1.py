class RandomizedSet:
    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            index = len(self.array)
            self.array.append(val)
            self.hashmap[val] = index
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap[val]
            last = self.array[-1]
            self.hashmap[last] = index
            self.array[index] = last
            self.array.pop()
            del self.hashmap[val]
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.array)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()