class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            hit -> hot, lit
            lit -> lin
            hot -> 1, 2, 3
            2 -> lin
            lin -> None
        """
        if endWord not in wordList:
            return 0
        
        n = len(wordList)
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj_list[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nxt_word in adj_list[pattern]:
                        if nxt_word not in visited:
                            q.append(nxt_word)
                            visited.add(nxt_word)
            count += 1
        return 0
