def solve(mat, listP):
    for i in listP:
        for r in range(3):
            for c in range(3):
                if mat[r][c] == i:
                    mat[r][c] = -1
    
    # Check rows
    for i in range(3):
        if mat[i][0] == -1 and mat[i][1] == -1 and mat[i][2] == -1:
            return "Yes"
    
    # Check columns
    for j in range(3):
        if mat[0][j] == -1 and mat[1][j] == -1 and mat[2][j] == -1:
            return "Yes"
            
    # Check main diagonal
    if mat[0][0] == -1 and mat[1][1] == -1 and mat[2][2] == -1:
        return "Yes"
    
    # Check anti-diagonal:
    if mat[0][2] == -1 and mat[1][1] == -1 and mat[2][0] == -1:
        return "Yes"
        
    return "No"

def main():
    mat = [[0 for j in range(3)] for i in range(3)]
    for i in range(3):
        mat[i] = [int(x) for x in input().split()]
    n = int(input())
    
    listP = []
    
    for i in range(n):
        c = int(input())
        listP.append(c)
    
    print(solve(mat, listP))
    
main()