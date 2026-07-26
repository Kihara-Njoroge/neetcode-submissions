class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in results:
                results[key] = []
            results[key].append(word)
            
        return list(results.values())