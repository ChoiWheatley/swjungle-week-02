import sys

N = int(input())
K = int(input())
alist = [tuple(map(int,input().split())) for _ in range(K)]
L = int(input())
dist = [input().split() for _ in range(L)]

dtable = [0]*(10001) # 방향전환에 사용되는 룩업테이블
for sec,turn in dist:
    dtable[int(sec)]=turn
#상중하중
di,dj = [-1,0,1,0], [0,1,0,-1] #시계방향으로 방향 정의
dr=1 #오른쪽 방향
snake = [(1,1)] #좌측상단
ans = 0 #0초

while True:
    ans +=1 #1초 경과
    ci,cj = snake[0] #현재 머리의 좌표
    ni,nj = ci+di[dr], cj+dj[dr] # 진행방향으로 한칸 이동
    #벽에 부딪혔거나, 뱀 몸에 부딪힌경우 종료
    if 1<=ni<=N and 1<=nj<=N and (ni,nj) not in snake:
        snake.insert(0,(ni,nj)) #머리위치[0]에 이동좌표 확장
        if (ni,nj) in alist:
            alist.remove((ni,nj))
        else:
            snake.remove((snake[-1])) # 꼬리부분 제거
        #방향전환
        if dtable[ans]=='D': #우회전
            dr = (dr+1)%4
        elif dtable[ans]=='L': #좌회전
            dr = (dr+3)%4
    else:
        break
print(ans)


