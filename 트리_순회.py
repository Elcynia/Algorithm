import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
tree = {}

for _ in range(n):
    node, l, r = input().split()
    tree[node] = [l, r]

def 전위(node):
    if node == '.':
        return
    print(node, end='')
    전위(tree[node][0])
    전위(tree[node][1])

def 중위(node):
    if node == '.':
        return
    중위(tree[node][0])
    print(node, end='')
    중위(tree[node][1])

def 후위(node):
    if node == '.':
        return
    후위(tree[node][0])
    후위(tree[node][1])
    print(node, end='')

전위('A')
print()
중위('A')
print()
후위('A')