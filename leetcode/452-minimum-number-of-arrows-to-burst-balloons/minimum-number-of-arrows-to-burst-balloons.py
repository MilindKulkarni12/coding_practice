class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points = sorted(points, key=lambda x: (x[1])) 
        # # points.sort()
        # print(points)
        # arrows = 0
        # i=0
        # while i < len(points):
        #     x1, x2 = points[i]
        #     dist = x2 - x1
        #     print(x1,x2)
        #     print("init i : ", i)
        #     print("dist", dist)
        #     while i < len(points)-1 and points[i+1][1] > x1:
        #         i += 1
        #         if points[i][1] - points[i][0] < dist:
        #             dist = points[i][1] - points[i][0]
        #             x1 = points[i][0]
        #         print("i : ", i)
        #     arrows += 1
        #     i += 1
        #     print("arrows : ", arrows)
        # return arrows

        #sorted_points=sorted(points, key=lambda x:x[1])
        points.sort(key=lambda x:x[1])
        #print(points)
        last=float('-inf')
        ans=0
        for point in points:
            start=point[0]
            end=point[1]
            if start>last:
                ans=ans+1
                last=end
        return ans
