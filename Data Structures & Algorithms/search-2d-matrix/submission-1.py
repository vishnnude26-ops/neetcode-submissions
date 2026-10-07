class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_pointer, right_pointer = (0, len(matrix) - 1)

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) //2
            inner_left_pointer, inner_right_pointer = 0, len(matrix[middle_pointer]) - 1
            if (matrix[middle_pointer][inner_left_pointer] <=
                                 target <= 
                matrix[middle_pointer][inner_right_pointer]):
                    while inner_left_pointer <= inner_right_pointer:
                        inner_middle_pointer = ( inner_left_pointer + inner_right_pointer ) // 2

                        if matrix[middle_pointer][inner_middle_pointer] == target: return True
                        elif matrix[middle_pointer][inner_middle_pointer] < target: inner_left_pointer = inner_middle_pointer + 1
                        else: inner_right_pointer = inner_middle_pointer - 1
                    return False
            elif matrix[middle_pointer][inner_right_pointer] < target: left_pointer = middle_pointer + 1
            else: right_pointer = middle_pointer - 1
        return False

