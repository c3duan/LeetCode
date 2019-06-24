from typing import List

class Solution:
    # Time Complexity: O(n/2)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            temp = s[i]
            s[i] = s[n - 1 - i]
            s[n - 1 - i] = temp