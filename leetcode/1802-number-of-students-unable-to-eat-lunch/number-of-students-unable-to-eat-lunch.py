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
                if students[i % n] == -4:
                    return n - j
                students.append(students[i])
                students[i % n] -= 1
                i += 1
        return 0

            
