class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for element in row:
                if element in seen and element != '.':
                    return False
                seen.add(element)
            
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                seen.add(board[j][i])
        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                # r_start and c_start are the top-left coordinates of the current 3x3 block
                
                seen = set()
                
                # Inner loops to iterate through the elements within the current 3x3 block
                for i in range(r_start, r_start + 3):
                    for j in range(c_start, c_start + 3):
                        element = board[i][j]
                        
                        # Check for duplicates, ignoring the '.' placeholder
                        if element != '.' and element in seen:
                            return False
                        
                        seen.add(element)
        return True


                