class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)
        for i in range(length):
            k = target - nums[i]
            if k in hashmap:
                return [i, hashmap[k]]
            hashmap[nums[i]] = i
