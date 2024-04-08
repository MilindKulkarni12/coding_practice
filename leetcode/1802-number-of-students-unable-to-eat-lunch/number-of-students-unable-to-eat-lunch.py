class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        j = 0
        n = len(students)
        while j < n:
            if students[i] == sandwiches[j]:
                i += 1
                j += 1
            else:
                students.append(students[i])
                i += 1
            if i > n*n:
                return n - j
        return 0

            
