import sys
n = int(sys.stdin.readline())

stack=[]


for _ in range(n):    
    stack.append(int(sys.stdin.readline()))

count=1
last = stack[-1]
for i in range(n-2,-1,-1):# 뒤에서 부터 -1이전까지,-1만큼
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)