package basic_study;

/** do-while문
 * do {
 *     Statement1;
 * } while (조건식);
 * Statement2;
 */

public class JAVA_03_6_do_while {
    public static void main(String args[]) {
        int i = 102;
        int sum = 0;
        do {
            if ((i % 2) == 0) {
                sum += i;
            }
            ++i;
        } while (i <= 100);
        System.out.println("1~100 사이 짝수의 합: " + sum);
    }
}
