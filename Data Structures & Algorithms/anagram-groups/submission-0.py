class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        visited = set()


        for i in range(len(strs)):
            if i in visited:
                continue

            group = [strs[i]]

            visited.add(i)

            for j in range(i+1, len(strs)):
                if j not in visited and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited.add(j) 

            result.append(group)

        return result