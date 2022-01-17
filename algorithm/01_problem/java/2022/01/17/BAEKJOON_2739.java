import java.util.Scanner;

// public class Main
public class BAEKJOON_2739 {
    public static void main(String args[]) throws Exception {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        for (int i = 1; i < 10; i++) {
            int res = i * N;
            System.out.println(N + " * " + i + " = " + res);
        }
    }
}
