n,s = map(int, input().split())
arr = list(map(int, input().split()))
left = right = 0
add = arr[0]
length = n + 1

while left <= right < n-1:
    if add < s:
        right += 1
        add += arr[right]
    else:
        length = min(length, right - left + 1)
        left += 1
        add -= arr[left]
print(0 if length == n+1 else length)