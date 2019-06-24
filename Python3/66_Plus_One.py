from typing import List

class Solution:
    # Time Complexity:
    # Best Case: O(1)
    # Asymtopic: O(n)
    # Worst Case: O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
                
        while i >= 0:
            digit = digits[i] + 1
            if digit > 9:
                digits[i] = 0
                i -= 1
                if i < 0:
                    digits.insert(0, 1)
            else:
                digits[i] = digit
                break
                
        return digits
                    