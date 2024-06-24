def lower_bound(arr, key):
    l, h, ans = 0, len(arr) - 1, -1
    
    while l <= h:
        m = l + ((h - l) >> 1)
        
        if arr[m] >= key:
            ans, h = m, m - 1
        else:
            l = m + 1
    
    ans = h if ans == -1 else ans
    
    return ans

def main():
    n = int(input())
    li = list(map(int, input().split()))
    k, x = map(int, input().split())
    ans = [0 for i in range(k)]
    
    idx = lower_bound(li, x)
    h = idx + 1
    
    while h - idx - 1 < k:
        if idx >= 0 and h < n:
            if x - li[idx] <= li[h] - x:
                idx -= 1
            else:
                h += 1
        elif idx >= 0:
            idx -= 1
        else:
            h += 1
    
    idx += 1
        
    print(' '.join(map(str, li[idx:h])))

main()