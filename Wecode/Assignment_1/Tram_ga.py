def check(r, c, mat):
    ddir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    mdir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    for i in range(4):
        u = r + ddir[i][0]
        v = c + ddir[i][1]
        
        if u >= 0 and u < 2 and v >= 0 and v < 2 and mat[u][v] == '#':
            vcr = 0
            for j in range(4):
                x = r + mdir[j][0]
                y = c + mdir[j][1]
                if x >= 0 and x < 2 and y >= 0 and y < 2 and mat[x][y] == '#':
                    vcr = 1
                    break
            return vcr

def solve(mat):
    
    for i in range(2):
        for j in range(2):
            if mat[i][j] == '.':
                continue
            if check(i, j, mat) == 0:
                return 0
    
    return 1

def main():
    mat = ["" for i in range(2)]
    
    for i in range(2):
        mat[i] = input()
    
    if solve(mat) == 1:
        print("Yes")
    else:
        print("No")

main()