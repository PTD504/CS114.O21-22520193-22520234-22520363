def lower_bound(arr, key):
    l, h = 0, len(arr) - 1
    
    while l <= h:
        m = l + ((h - l) >> 1)
        if arr[m] == key:
            return 1
        elif arr[m] > key:
            h = m - 1
        else:
            l = m + 1
    
    return 0

def main():
    m, n = map(int, input().split())
    allUser = list(map(int, input().split()))
    friends = list(map(int, input().split()))
    
    ans = 0
    
    for i in friends:
        if i > allUser[-1] or i < allUser[0]:
            continue
        if lower_bound(allUser, i) == 1:
            ans += 1
    
    print(ans)

main()