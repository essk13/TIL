package basic_study;

/**
 * 명시적 형변환
 */

public class JAVA_01_6_명시적_형변환 {
    public static void main(String args[]) {
        byte b1;
        char c1;
        int i1 = 128;
        int i2 = 97;
        double d1 = 3.14;

        System.out.println("명시적 형변환 결과");

        b1 = (byte) i1;
        System.out.println("b1 = (byte)i1의 형변환: " + b1);

        c1 = (char) i2;
        System.out.println("c1 = (char)i2의 형변환: " + c1);

        i1 = (int) d1;
        System.out.println("i1 = (double)d1의 형변환: " + i1);
    }
}
