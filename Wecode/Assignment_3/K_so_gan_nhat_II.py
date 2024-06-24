def lower_bound(arr, x):
    l, h, ans = 0, len(arr) - 1, -1
    
    while l <= h:
        m = l + (h - l) // 2
        
        if arr[m] >= x:
            ans, h = m, m - 1
        else:
            l = m + 1
    
    return ans if ans != -1 else h

def solve(arr, k, x):
    idx = lower_bound(arr, x)
    h = idx + 1
    
    while h - idx - 1 < k:
        if h < len(arr) and idx >= 0:
            if arr[idx] > arr[h]:
                h += 1
            else:
                idx -= 1
        elif idx >= 0:
            idx -= 1
        else:
            h += 1
    
    return (arr[idx + 1], arr[h - 1])
                

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    while True:
        try:
            k, x = map(int, input().split())
        except ValueError:
            break
        
        print(' '.join(map(str, solve(arr, k, x))))

if __name__ == '__main__':
    main()