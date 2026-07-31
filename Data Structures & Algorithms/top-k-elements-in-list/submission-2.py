class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        l = list(cnt.keys())
        l.sort(key= lambda x: cnt[x], reverse=True)
        return l[:k]