import java.io.*;

// public class Main
public class BAEKJOON_1330_Buffered {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] numbers = br.readLine().split(" ");
        int A = Integer.parseInt(numbers[0]);
        int B = Integer.parseInt(numbers[1]);

        // 중첩 삼항 연산자
        System.out.println((A > B) ? ">" : ((A < B) ? "<" : "=="));
    }
}
