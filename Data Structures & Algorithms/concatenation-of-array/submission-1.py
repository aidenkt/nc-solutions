class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list = nums.copy()
        for i in nums:
            list.append(i)
        return list