'''
백준 문제 링크 https://www.acmicpc.net/problem/4673

-- 문제 --
    양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수 더하는 함수
    ex) d(33) = 33 + 3 + 3 = 39
    n을 d(n)의 생성자라고 하는데, 생성자가 없는 경우 셀프넘버라고 한다.
    ex) 33은 39의 생성자이다.
-- 출력 --
    10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력
'''

# d(n)계산
def calc_dn(num):
    sum = num
    for i in range(len(str(num))):
        sum += int(str(num)[i])
        
    return sum

# self number인지 확인
def check_selfnumber(num):
    return num == 0
    
arr = [0] * 9999

# dn 계산하고 arr에 적용
for num in range(1, 10001):
    dn = calc_dn(num)
    if dn < 10000:
        arr[dn-1] = 1

# 출력
for num in range(len(arr)):
    if arr[num] == 0:
        print(num+1)
