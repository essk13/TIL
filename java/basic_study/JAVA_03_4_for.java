package basic_study;

/** for 문
 * for (초기식; 조건식; 증감식) {
 *     Statement1;
 * }
 * Statement2;
 */

public class JAVA_03_4_for {
    public static void main(String args[]) {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            if ((i % 2) == 0) {
                sum += i;
            }
        }
        System.out.println("1~100 사이 짝수의 합: " + sum);
    }
}
