ans = 0

def solve(mat, r, c):
    global ans
    rdir, cdir = [-1, 0, 1, 0], [0, -1, 0, 1]
    check = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '#' or check[i][j] == 1:
                continue
            q = []
            check[i][j] = 1
            q.append([i, j])
            
            while len(q) != 0:
                t = q.pop(0)
                
                for k in range(4):
                    x, y = t[0] + rdir[k], t[1] + cdir[k]
                    
                    if x >= 0 and y >= 0 and x < r and y < c and check[x][y] == 0 and mat[x][y] == '-':
                        check[x][y] = 1
                        q.append([x, y])
            ans += 1

def main():
    global ans
    test = 1
    
    while 1:
        try:
            r, c = map(int, input().split())
        except:
            break
        
        mat = [""] * r
        
        for i in range(r):
            mat[i] = input()
        
        solve(mat, r, c)
        
        print("Case " + str(test) + ": " + str(ans))
        
        ans, test = 0, test + 1

main()