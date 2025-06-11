/**
 * 백준 문제 링크 https://www.acmicpc.net/problem/2720
 * -- 입력 --
 * 테스트케이스 개수, 거스름돈 (센트단위)
 * -- 출력 --
 * 쿼터 (25센트), 다임 (10센트), 니켈 (5센트), 페니의 개수 (1센트)
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] coinAmounts = {25, 10, 5, 1}; // 동전의 금액 배열
        int caseCnt = 0; // 테스트 케이스 개수
        int changeAmount = 0; // 거스름돈
        StringBuffer resultText = new StringBuffer(); // 출력 텍스트

        // 테스트 케이스의 개수 입력 받기
        caseCnt = Integer.parseInt(br.readLine());

        for (int i = 0; i < caseCnt; i++) {
            // 거스름돈 입력 받기
            changeAmount = Integer.parseInt(br.readLine());

            // 동전 개수 계산
            for (int coin : coinAmounts) {
                resultText.append(changeAmount / coin).append(" "); // 각 동전별 개수 계산
                changeAmount %= coin; // 남은 거스름돈 저장
            }

            resultText.append("\n"); // 테스트케이스 하나 끝날때마다 줄 바꿈
        }

        // 출력
        System.out.println(resultText);
    }
}