def main():
    
    rdir, cdir = [-1, 0, 1, 0], [0, -1, 0, 1]
    
    r, c = map(int, input().split())
    
    mat = [[0] * c] * r
    
    for i in range(r):
        mat[i] = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                continue
            
            ans += 4
            
            for k in range(4):
                x, y = i + rdir[k], j + cdir[k]
                
                if x >= 0 and y >= 0 and x < r and y < c and mat[x][y] == 1:
                    ans -= 1
    
    print(ans)

main()