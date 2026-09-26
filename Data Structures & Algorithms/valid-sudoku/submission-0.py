from collections import defaultdict
from typing import List, Dict, Set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: Dict = defaultdict(set)
        columns: Dict = defaultdict(set)
        square: Dict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_element: str = board[r][c]
                if current_element == '.': continue

                elif (
                        current_element in rows[r] or 
                        current_element in columns[c] or 
                        current_element in square[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        
        return True