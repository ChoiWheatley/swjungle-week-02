import sys
n = int(sys.stdin.readline())

stack=[]

for _ in range(n):    
    stack.append(int(input()))



count=1
last = stack[-1]
for i in range(len(stack)):
    if stack[-i] > last:
        count += 1
        last = stack[i]

print(count)