class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]

        if len(v1) != len(v2):
            while len(v1) < len(v2):
                v1.append(0)
            while len(v2) < len(v1):
                v2.append(0)

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0

        