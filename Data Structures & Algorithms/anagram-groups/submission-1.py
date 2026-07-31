class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        def anagrams(s, t):
            if len(s) != len(t):
                return False

            l = [0] * 26
            for i in range(len(s)):
                l[ord(s[i]) - ord('a')] += 1
                l[ord(t[i]) - ord('a')] -= 1
            for num in l:
                if num != 0:
                    return False
            return True

    
        visited = set()
        for i in range(len(strs)):
            stepArray = [strs[i]]
            if i in visited:
                continue
            for j in range(i+1, len(strs)):
                if anagrams(strs[i], strs[j]) and j not in visited:
                    stepArray.append(strs[j])
                    visited.add(j)
            result.append(stepArray)
            visited.add(i)

        return result