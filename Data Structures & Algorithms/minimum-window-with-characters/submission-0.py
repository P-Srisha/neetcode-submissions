class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        length = len(s)
        i = 0
        j = 0
        result = ""

        need = Counter(t)
        window = Counter()

        required = len(need)
        formed = 0

        i, j = 0, 0
        start = 0
        minL = 1001

        while (j < length):
            window[s[j]] += 1
            if s[j] in need and need[s[j]] == window[s[j]]:
                formed += 1
            
            while formed == required:
                if j - i + 1 < minL:
                    start = i
                    minL = j - i + 1
                window[s[i]] -= 1
                if s[i] in need and need[s[i]] > window[s[i]]:
                    formed -= 1
                i += 1
            j += 1
        if minL == 1001:
            return ""

        return s[start : start + minL]