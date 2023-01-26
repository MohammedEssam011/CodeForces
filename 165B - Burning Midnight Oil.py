n, k =map(int,input().split())
left, right = 1, n
while left != right:
    x = middle = (left + right) // 2
    sum = 0
    while x != 0:
        sum += x
        x //= k
    if sum >= n:
        right = middle
    else:
        left = middle + 1
print(left)
