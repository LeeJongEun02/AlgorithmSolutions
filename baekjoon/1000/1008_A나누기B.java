/**
 * 백준 1008번 문제
 * 브론즈 5 / A / B
 * 두 수를 입력받고 나눗셈을 한 결과를 출력하는 문제 (상대오차가 10-9 이하)
 * 입력 : 1 / 3
 * 출력 : 0.33333333...
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double num1 = Double.parseDouble(st.nextToken());
        double num2 = Double.parseDouble(st.nextToken());

        System.out.println(num1 / num2);
    }
}
