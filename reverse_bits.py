class Solution:
    def reverseBits(self, n: int) -> int:
        val = bin(n)[2:]
        val = val.zfill(32)
        val = val[::-1]
        val = int(val, 2)
        return val