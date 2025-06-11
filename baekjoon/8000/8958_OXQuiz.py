'''
백준 문제 링크 https://www.acmicpc.net/problem/8958
   
--문제--
    문제가 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
    O O X X O X X O O O의 점수는
    1+2+0+0+1+0+0+1+2+3 = 10점이다.
    
--입력--
    첫째 줄에 테스트 케이스의 개수
    둘째 줄부터는 각 테스트 케이스가 한줄로 이루어져있다. 0~80정도의 길이

--출력--
    각 테스트 케이스마다 점수 출력
'''

'''
    testcase_count : 테스트 케이스 개수
    testcases : 테스트 케이스 리스트
    scores : 점수 리스트
'''
testcase_count = int(input())
testcases = []
scores = []

# 입력
for line in range(testcase_count):
    testcases.append(input())

# 계산
for testcase in testcases:
    '''
        total_score : 총 점수
        answer_count : 정답 개수
    '''
    total_score = 0
    answer_count = 0
  
    for num in range(len(testcase)):
        # OX퀴즈 결과
        result = testcase[num]

        # 퀴즈 결과가 O일 경우
        if result == 'O':
            answer_count += 1
            total_score += answer_count
        # 퀴즈 결과가 X일 경우
        else:
            answer_count = 0
  
    print(total_score)
      
