class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 0x00000001) 
            n = n >> 1
        return res