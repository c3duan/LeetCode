class Solution:
    # Time Complexity: O(1)
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        c = a + b
                
        return bin(c)[2:]