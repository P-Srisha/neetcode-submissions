class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # if (l == r):
        #     if (matrix[l][r] == target):
        #         return True
        #     else:
        #         return False

        while (l <= r):
            mid = (l + r) // 2
            
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                l1 = 0
                r1 = len(matrix[mid]) - 1

                while (l1 <= r1):
                    mid1 = (l1 + r1) // 2
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] < target:
                        l1 = mid1 + 1
                    else:
                        r1 = mid1 - 1    
                return False            
        return False