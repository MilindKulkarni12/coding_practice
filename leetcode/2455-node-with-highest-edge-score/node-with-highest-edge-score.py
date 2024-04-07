class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = defaultdict(int)
        max_score_idx, max_score = -1, -1
        for i in range(len(edges)):
            scores[edges[i]] += i
            if scores[edges[i]] > max_score:
                max_score = scores[edges[i]]
                max_score_idx = edges[i]
            elif scores[edges[i]] == max_score:
                max_score_idx = min(max_score_idx, edges[i])
        # print(scores, max_score, max_score_idx)
        # return list(sorted(scores.items(), key=lambda x: (x[1], -x[0]), reverse=True))[0][0]
        return max_score_idx
