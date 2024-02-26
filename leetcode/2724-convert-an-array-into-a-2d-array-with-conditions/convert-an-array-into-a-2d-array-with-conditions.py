class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        rows = max(freq.values())
        # print(mat)
        mat = []
        for k in freq.keys():
            if freq[k] > 0:
                for i in range(freq[k]):
                    if i < len(mat):
                        mat[i].append(k)
                    else:
                        mat.append([k])
                freq[k] = 0
        return mat
