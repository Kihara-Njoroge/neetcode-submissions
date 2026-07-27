class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for num, freq in sorted_items[:k]:
            res.append(num)

        return res