class Solution {
    public List<List<String>> solveNQueens(int n) {
       List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        
        // Initialize board with '.' (empty cells)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        
        // Start backtracking from row 0
        backtrack(board, 0, result);
        return result;
    }
    
    private void backtrack(char[][] board, int row, List<List<String>> result) {
        // BASE CASE: All queens placed successfully
        if (row == board.length) {
            result.add(construct(board));  // Convert board to List<String>
            return;
        }
        
        // Try placing queen in each column of current row
        for (int col = 0; col < board.length; col++) {
            if (isSafe(board, row, col)) {
                // CHOOSE: Place queen
                board[row][col] = 'Q';
                
                // EXPLORE: Move to next row
                backtrack(board, row + 1, result);
                
                // UNCHOOSE: Remove queen (backtrack)
                board[row][col] = '.';
            }
        }
    }
    
    private boolean isSafe(char[][] board, int row, int col) {
        int n = board.length;
        
        // Check 1: Same column (above current row)
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }
        
        // Check 2: Left diagonal (upper-left)
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Check 3: Right diagonal (upper-right)
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        return true;  // Safe to place queen
    }
    
    // Helper: Convert char[][] to List<String>
    private List<String> construct(char[][] board) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            result.add(new String(board[i]));  // Convert char[] to String
        }
        return result;
    }
}
