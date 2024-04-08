class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        j = 0
        last_found_i = -1
        n = len(students)
        print(n)
        while j < n:
            # print('i:', i, 'students[i]:', students[i], 'j:', j, 'sandwiches[j]:', sandwiches[j], last_found_i)
            
            if students[i] == sandwiches[j] and students[i] != -1:
                students[i] = -1
                last_found_i = i
                i = (i + 1) % n
                j += 1
            elif i == n-1 and last_found_i == -1:
                return n
            else:
                if i == last_found_i:
                    return n - j
                i = (i + 1) % n
        return 0

            
""" 



"""