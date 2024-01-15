from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for num in nums:
            if num >= target:
                return index
            index += 1
        return index

checker = Solution()
result = checker.searchInsert([2,3,4,5], 9)

print(result)
