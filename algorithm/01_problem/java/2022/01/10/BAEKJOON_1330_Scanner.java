import java.util.Scanner;

// public class Main
public class BAEKJOON_1330_Scanner {
    public static void main(String args[]) throws Exception {
        Scanner in = new Scanner(System.in);

        int A = in.nextInt();
        int B = in.nextInt();

        in.close();

        if (A > B) {
            System.out.println(">");
        } else if (A < B) {
            System.out.println("<");
        } else {
            System.out.println("==");
        }
    }
}
