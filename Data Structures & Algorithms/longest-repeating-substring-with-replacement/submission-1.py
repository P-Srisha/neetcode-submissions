class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        i = 0
        j = 1
        length = len(s)
        maxL = 1
        l = 1
        maxF = 1
        freq = {}
        freq[s[0]] = 1

        while (j < length):
            freq[s[j]] = 1 + freq.get(s[j], 0)
            maxF = max(maxF, freq[s[j]])
            while i < j and (j - i + 1) - maxF > k:
                freq[s[i]] -= 1
                i += 1
            maxL = max(maxL, j - i + 1)
            j += 1
        return maxL
            