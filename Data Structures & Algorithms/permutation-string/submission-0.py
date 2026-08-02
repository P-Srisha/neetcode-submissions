class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        length = len(s2)
        i = 0
        j = 0
        need = Counter(s1)
        window = Counter()

        while (j < length):
            window[s2[j]] += 1

            if j - i + 1 > len(s1):
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    del window[s2[i]]
                i += 1
            
            if need == window:
                return True
            j += 1

        return False