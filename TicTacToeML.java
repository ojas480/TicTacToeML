public class TicTacToeML {
    private static String[][] board;

    public static void main(String[] args) {
        board = new String[3][3];
        clearBoard();
        for (int i = 0; i < 100; i++) {
            makeMoveX();
            makeMoveY();
            makeMoveX();
            makeMoveY();
            makeMoveX();
            makeMoveY();
            System.out.println(isGameOver());
            printBoard();
            clearBoard();
        }
        

        //printBoard();
    }

    public static void makeMoveX () {
        String[][] newBoard = board;
        int xCord = (int) (Math.random()*3);
        int yCord = (int) (Math.random()*3);
        while (board[xCord][yCord].equals("X") || board[xCord][yCord].equals("Y")) {
            xCord = (int) (Math.random()*3);
            yCord = (int) (Math.random()*3);
        }
        newBoard[xCord][yCord] = "X";
        board = newBoard;
    }

    public static void makeMoveY() {
        String[][] newBoard = board;
        int xCord = (int) (Math.random()*3);
        int yCord = (int) (Math.random()*3);
        while (board[xCord][yCord].equals("X") || board[xCord][yCord].equals("Y")) {
            xCord = (int) (Math.random()*3);
            yCord = (int) (Math.random()*3);
        }
        newBoard[xCord][yCord] = "Y";
        board = newBoard;
    }


    /**
     * Returns cleared board.
     * @param board takes in board.
     * @return returns new cleared board.
     */
    public static void clearBoard() {
        String[][] newBoard = new String[3][3];
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[i].length; j++)
                newBoard[i][j] = " ";

        board = newBoard;
    }
    /**
     * Returns boolean representing wether or not game is over.
     * @param board Takes in String[][] board.
     * @return Returns boolean wether game is over.
     */
    public static boolean isGameOver() {
        String X = "XXX";
        String Y = "YYY";
        return  (board[0][0] + board[0][1] + board[0][2]).equals(X) || (board[0][0] + board[0][1] + board[0][2]).equals(Y) || 
                (board[1][0] + board[1][1] + board[1][2]).equals(X) || (board[1][0] + board[1][1] + board[1][2]).equals(Y) ||
                (board[2][0] + board[2][1] + board[2][2]).equals(X) || (board[2][0] + board[2][1] + board[2][2]).equals(Y) ||

                (board[0][0] + board[1][0] + board[2][0]).equals(X) || (board[0][0] + board[1][0] + board[2][0]).equals(Y) ||
                (board[0][1] + board[1][1] + board[2][1]).equals(X) || (board[0][1] + board[1][1] + board[2][1]).equals(Y) ||
                (board[0][2] + board[1][2] + board[2][2]).equals(X) || (board[0][2] + board[1][2] + board[2][2]).equals(Y) ||

                (board[0][0] + board[1][1] + board[2][2]).equals(X) || (board[0][0] + board[1][1] + board[2][2]).equals(Y) ||
                (board[0][2] + board[1][1] + board[2][0]).equals(X) || (board[0][2] + board[1][1] + board[2][0]).equals(Y);
    }
    /**
     * Prints out board
     * @param board Takes in String[][] board.
     */
    public static void printBoard() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                System.out.print("|" + board[i][j]);
            }
            System.out.println("|");
        }
    }

}