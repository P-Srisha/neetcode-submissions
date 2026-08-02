class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        j = 1
        length = len(s)
        maxL = 1
        l = 1
        seen = set()
        seen.add(s[0])

        while (j < length):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
    
            seen.add(s[j])
            maxL = max(maxL, j - i + 1)
            j += 1

        return maxL