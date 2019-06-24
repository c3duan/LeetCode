from typing import List

class Solution:
    # Time Complexity: O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        x = 0
        for i in range(1, n):
            if nums[i] != nums[x]:
                x += 1
                nums[x] = nums[i]
        return x + 1