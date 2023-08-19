# numbers에 있는 숫자를 하나씩 stack에 넣고 그 다음 숫자와 비교
# 만일 다음 숫자가 stack에 있는 숫자보다 크면 stack.pop()을 해주면서 가장 큰 숫자를 앞 쪽에 위치하도록 한다.
# k개 까지만 지워야 하므로 k > 0이상일 때만 수행하고, 만일 k개 미만으로 숫자를 지웠다면 뒤에 있는 숫자를 남은 k개 만큼 지우고 출력한다.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 정수 n과 k를 입력받음
numbers = input().rstrip()  # 문자열을 입력받고 오른쪽 공백과 개행 문자를 제거하여 numbers에 저장

stack = []  # 스택 초기화
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        # 스택이 비어있지 않고, 스택의 가장 위에 있는 숫자가 현재 숫자보다 작고, 아직 제거할 수 있는 횟수(k)가 남아있을 때
        stack.pop()  # 스택의 가장 위에 있는 숫자를 제거
        k -= 1  # 제거할 수 있는 횟수(k)를 1 감소
    stack.append(number)  # 현재 숫자를 스택에 추가

if k > 0:  # 만약 아직 제거할 수 있는 횟수가 남아있다면
    print(''.join(stack[:-k]))  # 스택에서 제거할 횟수만큼 문자를 제외하고 출력
else:
    print(''.join(stack))  # 그렇지 않으면 스택의 모든 문자를 출력