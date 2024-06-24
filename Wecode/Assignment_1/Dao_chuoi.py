def solve(s1, s2):
    n = len(s1)
    m = len(s2)
    
    if m != n:
        return "NO"
    
    a = [[0 for j in range(2)] for i in range(60)]
    b = [[0 for j in range(2)] for i in range(60)]
    
    for i in range(n):
        a[ord(s1[i]) - ord('A')][i & 1] += 1
        b[ord(s2[i]) - ord('A')][i & 1] += 1
        
    for i in range(60):
        if a[i][0] + a[i][1] != b[i][0] + b[i][1]:
            return "NO"
        if a[i][0] != b[i][0] or a[i][1] != b[i][1]:
            return "NO"
    
    return "YES"

def main():
    t = int(input())
    
    while t > 0:
        s1 = input()
        s2 = input()
        
        print(solve(s1, s2))
        
        t -= 1
main()

"""
phanthanhdang
ahphtnanhdang
ahthpnhnadgna
"""