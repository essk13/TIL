package basic_study;

/** 이차원 배열
 * 1. 이차원 배열 선언
 * 데이터 타입 + 배열 변수명 + [][]; >> int scoreList [][];
 * 데이터 타입 + [][] + 배열 변수명; >> int[][] scoreList;
 * 데이터 타입 + [] + 배열 변수명 + []; >> int[] scoreList [];

 * 2. 이차원 배열 객체 생성
 * 배열 변수명 = new + 데이터 타입 + [배열의 배열 길이] + [배열 길이]; >> scoreList = new int[3][4];
 * ※ 아래 두 항목 SET
 * 배열 변수명 = new + 데이터 타입 + [배열의 배열 길이] + []; >> scoreList = new int[3][];
 * 배열 변수명 + [인덱스 번호] = new + 데이터 타입 + [배열 길이];
 *     >> scoreList[0] = new int[4];
 *     >> scoreList[1] = new int[4];
 *     >> scoreList[2] = new int[4];
 */

public class JAVA_02_4_이차원배열 {
    public static void main(String args[]) {
        String[][] scoreList = new String[3][4];

        System.out.println("< 2차원 배열의 인덱스 출력 >");
        for (int i = 0; i < scoreList.length; i++) {
            for (int j = 0; j < scoreList[i].length; j++) {
                scoreList[i][j] = "[" + i + "][" + j + "] 요소";
                System.out.println(scoreList[i][j] + "\t");
            }
            System.out.println(" ");
        }
    }
}
