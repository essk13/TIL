import java.io.*;

// public class Main
public class BAKEJOON_9498 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int score = Integer.parseInt(br.readLine());

        System.out.println((score >= 90) ? "A" : ((score >= 80) ? "B" : ((score >= 70) ? "C" : ((score >= 60) ? "D" : "F"))));

        /*
            String ans;
            if (score >= 90)
                ans = "A";
            else if (score >= 80)
                ans = "B";
            else if (score >= 70)
                ans = "C";
            else if (score >= 60)
                ans = "D";
            else
                ans = "F";

            System.out.println(ans);
         */
    }
}
