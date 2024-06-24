def main():
    n = int(input())
    l = []
    
    for i in range(n):
        c = int(input())
        l.append(c)
    
    l.sort()
    
    ans = 0
    
    for i in range(1, n):
        ans += l[i] - l[i - 1] - 1
        
    print(ans)

main()