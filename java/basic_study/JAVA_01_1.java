package basic_study;

/**
 * 파일명 : JAVA_01.java
 * 작성일 : 2022/01/09
 * 작성자 : EK
 */
/* 다음 클래스는 다음과 같은 두 줄의 내용을 출력하는 자파 프로그램이다.
   "출렫될 내용은 다음과 같습니다."
   "처음 작성한 자바 프로그램입니다."
 */
public class JAVA_01_1 {
    static String s = "출력될 내용은 다음과 같습니다.\n";

    // 두 번째 줄에 내용을 출력하는 메서드 선언
    static String getMessage() {
        return "처음 작성한 자바 프로그램입니다.";
    }
    public static void main(String args[]) {
        System.out.println(s + getMessage()); // 도스 창 출력
    }
}