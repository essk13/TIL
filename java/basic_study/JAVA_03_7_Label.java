package basic_study;

/** Label (break, continue)
 * 특정 반복문 종료 (다중 반복의 경우 활용 가능)
 * break 반복문;
 * continue 반복문;
 */

public class JAVA_03_7_Label {
    public static void main(String args[]) {
        outer: for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 2)
                    break outer;
                System.out.println("i = " + i + " j = " + j);
            }
        }
    }
}
