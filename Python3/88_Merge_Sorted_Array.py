from typing import List

class Solution:
    # Time Complexity:
    # Best Case: O(n)
    # Asymtopic: O(n + m)
    # Worst Case: O(max(m,n)^2)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        end = m
        while i < (m+n) and j < n: 
            if nums1[i] < nums2[j]:
                if i >= end:
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
                else:
                    i += 1
            else:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums1[i+1:] = [temp] + nums1[i+1:(m+n-1)]
                end += 1
                i += 1
                j += 1
            