class Solution:
    def hammingWeight(self, n: int) -> int:
        rv = 0
        while n:
            rv += n & 0x00000001
            n = n >> 1
        return rv
            
    def modHammingWeight(self, n: int) -> int:
        rv = 0
        while n:
            rv  += n % 2
            n = n >> 1
        return rv

    def fastHammingWeight(self, n: int) -> int:
        rv = 0
        while n:
            print(bin(n))
            rv += 1
            n = n & (n - 1)
            
        return rv

    def scratch(self, i: int):
        j = i - ((i >> 1) & 0x55555555)
        k = j 
        print(bin(j))
        print(j)

# Solution().scratch(0b1111)

print(Solution().hammingWeight(0b1011))
print(Solution().modHammingWeight(0b1011))
print(Solution().fastHammingWeight(0b1011))