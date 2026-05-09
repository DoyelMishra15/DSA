from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.keyTable = {}
        self.freqTable = defaultdict(OrderedDict)
    def updateFreq(self, key):
        value, freq = self.keyTable[key]
        del self.freqTable[freq][key]
        if not self.freqTable[freq]:
            del self.freqTable[freq]
            if self.minFreq == freq:
                self.minFreq += 1
        self.keyTable[key] = (value, freq + 1)
        self.freqTable[freq + 1][key] = None
    def get(self, key: int) -> int:
        if key not in self.keyTable:
            return -1
        value, freq = self.keyTable[key]
        self.updateFreq(key)
        return value
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.keyTable:
            freq = self.keyTable[key][1]
            self.keyTable[key] = (value, freq)
            self.updateFreq(key)
            return
        if len(self.keyTable) == self.cap:
            evictKey, _ = self.freqTable[self.minFreq].popitem(last=False)
            del self.keyTable[evictKey]
            if not self.freqTable[self.minFreq]:
                del self.freqTable[self.minFreq]
        self.keyTable[key] = (value, 1)
        self.freqTable[1][key] = None
        self.minFreq = 1     


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
