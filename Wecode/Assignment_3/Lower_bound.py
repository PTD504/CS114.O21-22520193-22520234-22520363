def lower_bound(arr, key):
    l, h, ans = 0, len(arr) - 1, -1
    
    while l <= h:
        m = l + int((h - l) / 2)
        
        if arr[m] == key:
            ans, h = m, m - 1
        elif arr[m] > key:
            h = m - 1
        else:
            l = m + 1
    
    return ans

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    nArr = list(map(int, input().split()))
    
    for i in range(m):
        print(lower_bound(arr, nArr[i]))

main()