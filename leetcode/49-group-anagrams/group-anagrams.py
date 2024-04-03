class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams  = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(list(s)))
            anagrams[key].append(s)
        # print(anagrams)
        return anagrams.values()
