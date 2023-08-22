import sys

def bfs(si,sj,ei,ej):
    q = []
    v = [[0]*m for _ in range(n)]

    q.append([si,sj])
    v[si][sj]=1

    while q:
        ci,cj = q.pop(0)
        
        if (ci,cj) == (ei,ej):
            return v[ei][ej]

        #조건 4방향, 범위내, 조건에 맞으면 q에 삽입
        #arr==1, v==0  상,하,좌,우
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            #next i 좌표
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
 

n,m = map(int, input().split())

arr = [list(map(int,input())) for _ in range(n)]

ans = bfs(0,0,n-1,m-1)
print(ans)

