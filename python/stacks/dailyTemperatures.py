class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stak = [0]
        rv = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stak and temperatures[stak[-1]] < t:
                prev = stak.pop()
                rv[prev] = i - prev
            stak.append(i)
        return rv
