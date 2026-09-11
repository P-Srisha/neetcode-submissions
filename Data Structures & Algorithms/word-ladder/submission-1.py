class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        count = 0
        wordList.append(beginWord)
        adj = {word: [] for word in wordList}

        def countMatching(word1, word2):
            i = 0
            count = 0
            while i < len(word1):
                if word1[i] != word2[i]:
                    count += 1
                i += 1
            
            return count == 1

        def adjList(word):
            for w in wordList:
                if countMatching(w, word):
                    adj[word].append(w)

        for word in wordList:
            adjList(word)
        print(adj)

        visit = set()
        q = collections.deque([beginWord])
    
        def bfs():
            nonlocal count

            while q:
                count += 1
                for _ in range(len(q)):
                    # count += 1
                    w = q.popleft()
                    if w == endWord:
                        return w

                    visit.add(w)

                    for nei in adj[w]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

        lastWord = bfs()
        return count if lastWord == endWord else 0