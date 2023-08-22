import sys

tree = {}

n = int(sys.stdin.readline().strip())

for n in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root]=[left, right]

def pre(root):
    if root != '.':
        print(root, end='')#루트
        pre(tree[root][0])# 왼쪽
        pre(tree[root][1])# 오른쪽

def mid(root):
     if root != '.':   
        mid(tree[root][0])#왼쪽
        print(root,end='')#루트
        mid(tree[root][1])#오른쪽

def post(root):
    if root != '.':
        post(tree[root][0]) #왼쪽
        post(tree[root][1]) #오른쪽
        print(root,end='')#루트


pre('A')
print()
mid('A')
print()
post('A')