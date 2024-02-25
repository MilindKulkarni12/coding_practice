class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        mapping = {}
        for i in range(len(pattern)):
            if mapping.get(pattern[i], -1) == -1:
                mapping[pattern[i]] = words[i]
            elif mapping[pattern[i]] != words[i]:
                return False
        
        return len(list(set(mapping.keys()))) == len(list(set(mapping.values())))
