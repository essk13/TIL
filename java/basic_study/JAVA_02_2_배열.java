package basic_study;

/** 1차원 배열
 * 1. 배열 변수 선언
 * 데이터 타입 + 배열 변수명 + []; >> int scoreList[];
 * 데이터 타입 + [] + 배열 변수명; >> int[] scoreList;

 * 2. 배열 객체 생성
 * 배열 변수명 = new + 데이터 타입 + [배열의 길이]; >> scoreList = new int[100];

 * 3. 선언 + 생성
 * 데이터 타입 + 배열 변수명 + [] = new + 데이터 타입 + [배열의 길이]; >> int scoreList[] = new int[100];
 * 데이터 타입 + [] + 배열 변수명 = new + 데이터 타입 + [배열의 길이]; >> String[] nameList = new String[5];

 * 4. 선언 + 생성 + 초기화
 * 선언 = {초기값}; >> int[] scoreList = {45, 80, 100, 59, 80};
 * 배열 변수명 = 생성 + {초기값}; >> scoreList = new int[] {45, 80, 100, 59, 80};
 */

public class JAVA_02_2_배열 {
    public static void main(String args[]) {
        int[] scoreList;
        scoreList = new int[5];

        scoreList[0] = 80;
        scoreList[1] = 95;
        scoreList[2] = 68;
        scoreList[3] = 100;
        scoreList[4] = 54;
        System.out.println("scoreList 길이 = " + scoreList.length);

        System.out.println("< scoreList 배열 요소 출력 >");
        System.out.println(scoreList[0] + "\t");
        System.out.println(scoreList[1] + "\t");
        System.out.println(scoreList[2] + "\t");
        System.out.println(scoreList[3] + "\t");
        System.out.println(scoreList[4]);
    }
}
