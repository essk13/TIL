package basic_study;

public class JAVA_01_4 {
    boolean win;
    public void setWin(int s) {
        int score = s;
        if (score > 10) {
            win = true;
        }
    }
    public void printWinner() {
        if (win == true) {
            System.out.println("WINNER");
        } else {
            System.out.println("LOSER");
        }
    }
}
