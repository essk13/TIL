package basic_study;

public class JAVA_02_1_논리연산자 {
    public static void main(String args[]) {
        int num1 = 9;
        int num2 = 2;
        int num3 = 0;

        //&& 연산자 - 좌측 결과가 false인 경우 우측 연산 없이 false 리턴
        System.out.println((num1 == num2) && ((num1 / num3) > 0));

        // & 연산자 - 좌측 결과와 상관 없이 좌, 우 연산 모두 실행 >> 모두 참이면 true 반환
        // System.out.println((num1 == num2) & ((num1 / num3) > 0));

        // || 연산자 - 좌측 결과가 true인 경우 우측 연산 없이 true 리턴
        System.out.println((num1 != num2) || ((num1 / num3) > 0));

        // | 연산자 - 좌측 결과와 상관 없이 좌, 우 연산 모두 실행 >> 모두 거짓이면 false 반환
        // System.out.println((num1 != num2) | ((num1 / num3 > 0)));
    }
}
