class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i -1]:
                continue

            pairs = self.pair_sum_sorted(nums, 1+i, -nums[i])

            for pair in pairs:
                triplets.append([nums[i]] + pair)
        return triplets
        
    def pair_sum_sorted(self, nums: List[int], start: int, target: int) -> List[int]:
        seen = set()
        pairs = []
        prev_num = None

        for i in range(start, len(nums)):
            num = nums[i]
            diff = target - num

            if diff in seen:
                if num != prev_num:
                    pairs.append([diff, num])
                    prev_num = num
            seen.add(num)
        
        return pairs
