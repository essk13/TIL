package basic_study;

/** while문
 * while(조건식) {
 *     Statement1;
 * }
 * Statement2;
 */

public class JAVA_03_5_while {
    public static void main(String args[]) {
        int i = 1;
        int sum = 0;
        while (i <= 100) {
            if ((i % 2) != 0) {
                sum += i;
            }
            i++;
        }
        System.out.println("1~100 사이 홀수의 합: " + sum);
    }
}
