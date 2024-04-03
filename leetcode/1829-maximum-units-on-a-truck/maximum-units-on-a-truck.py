class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypesSorted = sorted(boxTypes, key=lambda x: (x[1], x[0]), reverse=True)
        # print(boxTypesSorted)
        i = 0
        total_units = 0
        while i < len(boxTypes) and truckSize > 0:
            # print(truckSize, i, total_units)
            box, units = boxTypesSorted[i]
            if box <= truckSize:
                total_units += box * units
                truckSize -= box
            else:
                total_units += truckSize * units
                truckSize = 0
            i += 1

        return total_units
