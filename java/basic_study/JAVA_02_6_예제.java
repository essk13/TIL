package basic_study;

public class JAVA_02_6_예제 {
    public static void main(String args[]) {
        // 점수 5개를 저장할 수 잇는 정수형 배열 생성
        int scoreList [] = new int[5];

        // 1. 명령행 매개변수로 들어온 5개의 점수를 배열에 저장
        scoreList[0] = Integer.parseInt(args[0]);
        scoreList[1] = Integer.parseInt(args[1]);
        scoreList[2] = Integer.parseInt(args[2]);
        scoreList[3] = Integer.parseInt(args[3]);
        scoreList[4] = Integer.parseInt(args[4]);

        // 2. 배열에 저장된 자바 점수의 총합 계산
        int totalScore = 0;
        totalScore = scoreList[0] + scoreList[1] + scoreList[2] + scoreList[3] + scoreList[4];

        // 3. 점수의 평균 계산
        double avgScore = 0.0;
        avgScore = (double) totalScore/scoreList.length;

        // 총합과 평균 출력
        System.out.println("총 점수: " + totalScore);
        System.out.println("평균 점수: " + avgScore);
    }
}
