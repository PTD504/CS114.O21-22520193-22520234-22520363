H, W, K = input().split()
H = int(H)
W = int(W)
K = int(K)
ans = 0

mat = ["" for i in range(H)]

def recursion(rows, cols, i, arr, allBlackCells):
    
    global ans
    
    for j in range(2):
        arr[i] = j
        
        if i == H + W - 1:
            kCells = 0
            for k in range(H):
                if arr[k] == 1:
                    kCells += rows[k]
            for k in range(H, H + W):
                if arr[k] == 1:
                    kCells += cols[k - H]
            for r in range(H):
                if arr[r] == 0:
                    continue
                for c in range(H, H + W):
                    if arr[c] == 1 and mat[r][c - H] == '#':
                        kCells -= 1
                        
            if allBlackCells - kCells == K:
                ans += 1
        else:
            recursion(rows, cols, i + 1, arr, allBlackCells)


def main():
    for i in range(H):
        mat[i] = input()
    
    rows = []
    cols = []
    allBlackCells = 0

    for i in mat:
        countBlackCells = 0
        for j in i:
            if j == '#':
                allBlackCells += 1
                countBlackCells += 1
        rows.append(countBlackCells)

    for j in range(W):
        countBlackCells = 0
        for i in range(H):
            if mat[i][j] == '#':
                countBlackCells += 1
        cols.append(countBlackCells)
    
    arr = [0 for i in range(H + W)]
    
    recursion(rows, cols, 0, arr, allBlackCells)
    
    print(ans)

main()