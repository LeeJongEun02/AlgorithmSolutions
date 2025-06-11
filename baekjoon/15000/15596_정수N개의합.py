'''
백준 문제 링크 https://www.acmicpc.net/problem/15596
   
--문제--
    정수 n개의 합을 구하는 함수 작성
    python 작성 함수
        - def solve(a: list) -> int
        - a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
        - 리턴값 : a에 포함되어 있는 정수 n개의 합
'''
def solve(a):
    ans = 0
    for num in a:
        ans += num
    return ans
