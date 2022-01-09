package basic_study;

public class JAVA_03_2_if_else_if {
    public static void main(String args[]) {
        int month = Integer.parseInt(args[0]);

        if (month == 3 || month == 4 || month == 5) {
            System.out.println(month + "월은 봄입니다.");
        } else if (month == 6 || month == 7 || month == 8) {
            System.out.println(month + "월은 여름입니다.");
        } else if (month == 9 || month == 10 || month == 11) {
            System.out.println(month + "월은 가을입니다.");
        } else {
            System.out.println(month + "월은 겨울입니다.");
        }
    }
}
