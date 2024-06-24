def solve(r, c, l, mat):
    for i in range(r):
        idx = 0
        st1 = ""
        for j in range(c):
            st2 = mat[i][j]
            while len(st2) < l[idx]:
                st2 = " " + st2
            if j != c - 1:
                st2 += " "
            st1 += st2
            idx += 1
        print(st1)

def main():
    r, c = map(int, input().split())
    
    mat = [""] * r
    
    for i in range(r):
        mat[i] = list(input().split())
    
    l = []
    
    for j in range(c):
        m = 0
        for i in range(r):
            t = int(mat[i][j])
            mat[i][j] = str(t)
            m = max(m, len(mat[i][j]))
        l.append(m)
    
    solve(r, c, l, mat)
    
main()