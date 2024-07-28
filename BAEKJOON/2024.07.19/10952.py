"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1 
1 1
2 3
3 4
9 8
5 2
0 0

예제 출력 1 
2
5
7
17
7
"""

while (True):       #바보처럼 for문에 True를 넣었는데 계속 if문의 조건식을 충족하지 않았음에도 불구하고 한 번 실행되고 종료가 됨. for문은 i부터 range 조건까지 반복적으로 실행되는데 True이기 때문에 참 즉, 1로 인식하여 한 번만 실행이 되는 것이 아닌가 싶음. 
    A, B = map(int, input().split())
    if (A == 0 and B == 0): 
        break
    else:
        print(A + B)        #실수로 들여쓰기를 안했는데 IndentationError: expected an indented block 에러가 남 즉, 저 에러는 해당 줄 들여쓰기 에러다.
    
print("종료")