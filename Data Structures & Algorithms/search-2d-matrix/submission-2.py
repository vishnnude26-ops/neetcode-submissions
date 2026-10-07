class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_pointer, right_pointer = (0, len(matrix) - 1)

        while left_pointer <= right_pointer:
            middle_pointer: int = (left_pointer + right_pointer) // 2

            inner_l_pointer, inner_r_pointer = (0, len(matrix[middle_pointer]) - 1)
            if (matrix[middle_pointer][inner_l_pointer] <= target <= matrix[middle_pointer][inner_r_pointer]):
                  
                  while inner_l_pointer <= inner_r_pointer:
                        inner_m_pointer: int = (inner_l_pointer + inner_r_pointer) // 2

                        if matrix[middle_pointer][inner_m_pointer] == target: return True
                        elif matrix[middle_pointer][inner_m_pointer] < target: inner_l_pointer = inner_m_pointer + 1
                        else: inner_r_pointer = inner_m_pointer - 1
                  return False
            elif matrix[middle_pointer][inner_r_pointer] < target: left_pointer = middle_pointer + 1
            else: right_pointer = middle_pointer - 1
        return False