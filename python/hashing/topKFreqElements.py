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


        

print(Solution().topKFrequent([1,2,2,3,4,4,4], 2))