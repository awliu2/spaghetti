from typing import List
from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        rv = []
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else: counts[i] += 1

        rv = sorted(counts, key = counts.get)[-k:]
        
        return rv
        """
        for j in range(0,k):
            maximum = max(counts, key = lambda key: counts[key])
            rv.append(maximum)
            counts.pop(maximum)
        """
        return rv

    def Bucket(self, nums: List[int], k: int) -> List[int]:
        print(f"k:{k}")
        counts = defaultdict(int)
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else: counts[i] += 1

        l = len(nums)

        freqsBucket = [[] for _ in range(l + 1)]
        for key,val in counts.items():
            freqsBucket[val].append(key)

        print(freqsBucket)
        bucketIdx = l
        rv = []
        while k > 0:
            while freqsBucket[bucketIdx] == []:
                bucketIdx -= 1
            for i in freqsBucket[bucketIdx]:
                print(k)
                if k == 0: 
                    break
                rv.append(i)
                k -= 1
            bucketIdx -= 1
            
        return rv

        
        
nums = [1,2,2,3,4,4,4]
# print(Solution().topKFrequent([1,2,2,3,4,4,4], 2))

print(Solution().Bucket([1,2,2,3,4,4,4],2))