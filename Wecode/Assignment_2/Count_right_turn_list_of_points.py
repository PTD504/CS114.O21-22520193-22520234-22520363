def main():
    n = int(input())
    l = []
    ans = 0
    
    for i in range(n):
        a, b = map(int, input().split())
        l.append([a, b])
    
    for i in range(2, n):
        x1, y1 = (l[i - 2][0], l[i - 2][1])
        x2, y2 = (l[i - 1][0], l[i - 1][1])
        x3, y3 = (l[i][0], l[i][1])
        
        v1, v2 = (x2 - x1) * (y3 - y2), (y2 - y1) * (x3 - x2)
        
        if v1 - v2 < 0:
            ans += 1
    
    print(ans)

main()