def swap_row(l, h, c, mat):
    for i in range(c):
        mat[l][i] ^= mat[h][i]
        mat[h][i] ^= mat[l][i]
        mat[l][i] ^= mat[h][i]

def main():
    r, c = map(int, input().split())
    
    mat = [[0] * c] * r
    
    for i in range(r):
        mat[i] = list(map(int, input().split()))
    
    l, h = 0, r - 1
    
    while l < h:
        swap_row(l, h, c, mat)
        l += 1
        h -= 1
        
    for i in range(r):
        print(" ".join(map(str, mat[i])))

main()