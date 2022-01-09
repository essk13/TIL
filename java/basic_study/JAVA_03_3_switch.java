package basic_study;

public class JAVA_03_3_switch {
    public static void main(String args[]) {
        int month = Integer.parseInt(args[0]);
        switch (month) {
            case 3:
            case 4:
            case 5:
                System.out.println(month + "월 = 봄");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println(month + "월 = 여름");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println(month + "월 = 가을");
                break;
            case 12:
            case 1:
            case 2:
                System.out.println(month + "월 = 겨울");
                break;
            default:
                System.out.println("해당 숫자는 월이 아닙니다.");
                break;
        }
    }
}
