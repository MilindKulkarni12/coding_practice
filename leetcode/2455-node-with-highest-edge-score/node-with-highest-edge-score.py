class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = defaultdict(int)
        for i in range(len(edges)):
            scores[edges[i]] += i
        # print(scores)
        return list(sorted(scores.items(), key=lambda x: (x[1], -x[0]), reverse=True))[0][0]
