import heapq

def main():
    n, m = map(int, input().split())
    arr = []
    x = 0
    
    for _ in range(n):
        arr.append(-int(input()))
    
    heapq.heapify(arr)
    
    for _ in range(m):
        l = list(map(int, input().split()))
        if l[0] == -1:
            heapq.heappop(arr)
        elif l[0] == -2:
            x = heapq.heappop(arr)
            while arr:
                if x == arr[0]:
                    heapq.heappop(arr)
                else:
                    break
        elif l[0] == -3:
            heapq.heapreplace(arr, arr[0] + l[1])
        else:
            y = l[1]
            x = arr[0]
            
            while True:
                if arr[0] != x:
                    break
                heapq.heapreplace(arr, x + y)
    
    while arr:
        print(-heapq.heappop(arr))

main()