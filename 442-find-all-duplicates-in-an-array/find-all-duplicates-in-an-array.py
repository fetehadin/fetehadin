class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0
        result = []
        while i < size:
            correct = nums[i]-1
            if nums[i]!= nums[correct]:
                nums[i],nums[correct]= nums[correct], nums[i]
            else:
                i+=1
        for i in range(size):
            if nums[i] != i+1:
                result.append(nums[i])
        return result