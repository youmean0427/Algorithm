import sys
input = sys.stdin.readline

N = int(input())

left = [0] * (N+1)
right = [0] * (N+1)
tree = {}
for i in range(1, N+1):

    x, y, z = map(str, input().split())
    tree[x] = [y, z]

preorder = []
inorder = []
postorder = []

def preorder_travers(T):
    if T != '.':
        preorder.append(T)
        preorder_travers(tree[T][0])
        preorder_travers(tree[T][1])
    return preorder

print("".join(preorder_travers('A')))

def inorder_travers(T):
    if T != '.':
        inorder_travers(tree[T][0])
        inorder.append(T)
        inorder_travers(tree[T][1])
    return inorder

print("".join(inorder_travers('A')))

def postorder_travers(T):
    if T != '.':
        postorder_travers(tree[T][0])
        postorder_travers(tree[T][1])
        postorder.append(T)
    return postorder

print("".join(postorder_travers('A')))