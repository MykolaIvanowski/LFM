class TimeMap:

    def __init__(self):
        self.key_store ={}

    def set(self, key: str, value: str, timestamp: int)-> None:
        if key not in self.key_store:
            self.key_store[key]=[]
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int)-> str:
        res = ""
        values = self.key_store.get(key,[])
        left, right = 0, len(values) - 1

        while left <= right:
            middle = (left + right)//2
            if values[middle][1] <= timestamp:
                res = values[middle][0] # the closest value we have
                left = middle+1
            else:
                right = middle-1

        return res


timeMap  =  TimeMap()

# store the key "alice" and value "happy" along with timestamp = 1.
timeMap.set("alice", "happy", 1)

timeMap.get("alice", 1)# return "happy"

# return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.get("alice", 2)

# store the key "alice" and value "sad" along with timestamp = 3.
timeMap.set("alice", "sad", 3)
print(timeMap.get("alice", 3))# return "sad"
