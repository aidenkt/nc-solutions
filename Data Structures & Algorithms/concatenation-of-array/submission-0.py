class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list = []
        for i in nums:
            list.append(i)
        for i in nums:
            list.append(i)
        return list