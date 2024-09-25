class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # i = 0
        # while i < len(haystack):
        #     flag = True
        #     start = i
        #     for j in range(len(needle)):
        #         print(haystack[start + j], needle[j])
        #         if (start + j >= len(haystack)) or (haystack[start + j] != needle[j]):
        #             flag = False
        #             break
        #         else:
        #             i += 1
        #     if flag:
        #         return start
        #     i =  
        # return -1
        return haystack.find(needle)