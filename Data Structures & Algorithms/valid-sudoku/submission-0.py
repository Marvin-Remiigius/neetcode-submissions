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
        print("Block 1")
        seen = set()
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 2")
        seen = set()
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 3")
        seen = set()
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 4")
        seen = set()
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 5")
        seen = set()
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 6")
        seen = set()
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 7")
        seen = set()
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 8")
        seen = set()
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])
        print("Block 9")
        seen = set()
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])

        return True


                