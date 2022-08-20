import collections

class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.times[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
                mid = (left + right) // 2
                if arr[mid][1] <= timestamp:
                    left = mid + 1
                elif arr[mid][1] > timestamp:
                    right = mid
        
        return "" if right == 0 else arr[right - 1][0]
                    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)