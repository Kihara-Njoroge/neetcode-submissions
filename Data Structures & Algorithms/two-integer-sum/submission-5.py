class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in seen:
                return [seen[diff], i]
            seen[numbers[i]] = i