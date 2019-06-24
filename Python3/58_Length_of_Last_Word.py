class Solution:
    # Time Complexity: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(' ')
        return len(words[-1])