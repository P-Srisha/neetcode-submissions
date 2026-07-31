class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in cnt.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                result.append(x)
                if (len(result) == k):
                    return result