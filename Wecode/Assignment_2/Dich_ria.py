def rotate(top_left, bottom_right, nums, mat):
    x1, y1, x2, y2 = top_left[0], top_left[1], bottom_right[0], bottom_right[1]
    
    if x1 == x2 and y1 == y2:
        return
    elif x1 == x2:
        if nums == 1:
            temp = mat[x1][y1]
            
            while y1 < y2:
                mat[x1][y1] = mat[x1][y1 + 1]
                y1 += 1
            
            mat[x1][y2] = temp
        else:
            temp = mat[x1][y2]
            
            while y1 < y2:
                mat[x1][y2] = mat[x1][y2 - 1]
                y2 -= 1
            
            mat[x1][y1] = temp
            
        return
    elif y1 == y2:
        if nums == 0:
            temp = mat[x2][y1]
            
            while x1 < x2:
                mat[x2][y1] = mat[x2 - 1][y1]
                x2 -= 1
            
            mat[x1][y1] = temp
        else:
            temp = mat[x1][y1]
            
            while x1 < x2:
                mat[x1][y1] = mat[x1 + 1][y1]
                x1 += 1
            
            mat[x2][y1]  = temp
        
        return
    
    li = []
    
    for i in range(y1, y2 + 1):
        li.append(mat[x1][i])
    for i in range(x1 + 1, x2 + 1):
        li.append(mat[i][y2])
    for i in range(y2 - 1, y1 - 1, -1):
        li.append(mat[x2][i])
    for i in range(x2 - 1, x1, -1):
        li.append(mat[i][y1])
    
    if nums == 1:
        j = 1
        n = len(li)
        
        for i in range(y1, y2 + 1):
            mat[x1][i] = li[j]
            j = (j + 1) % n
        for i in range(x1 + 1, x2 + 1):
            mat[i][y2] = li[j]
            j = (j + 1) % n
        for i in range(y2 - 1, y1 - 1, -1):
            mat[x2][i] = li[j]
            j = (j + 1) % n
        for i in range(x2 - 1, x1, -1):
            mat[i][y1] = li[j]
            j = (j + 1) % n
    else:
        n = len(li)
        j = n - 1
        
        for i in range(y1, y2 + 1):
            mat[x1][i] = li[j]
            j = (j + 1) % n
        for i in range(x1 + 1, x2 + 1, 1):
            mat[i][y2] = li[j]
            j = (j + 1) % n
        for i in range(y2 - 1, y1 - 1, -1):
            mat[x2][i] = li[j]
            j = (j + 1) % n
        for i in range(x2 - 1, x1, -1):
            mat[i][y1] = li[j]
            j = (j + 1) % n

def main():
    r, c = map(int, input().split())
    
    mat = [[0] * c] * r
    
    for i in range(r):
        mat[i] = list(map(int, input().split()))
    
    top_left = [0, 0]
    bottom_right = [r - 1, c - 1]
    nums = 0
    
    while top_left[0] <= bottom_right[0] and top_left[1] <= bottom_right[1]:
        rotate(top_left, bottom_right, nums, mat)
        top_left[0] += 1
        top_left[1] += 1
        bottom_right[0] -= 1
        bottom_right[1] -= 1
        nums = 1 - nums
    
    for i in range(r):
        print(" ".join(map(str, mat[i])))

main()

"""
5 4

1 2 3 4

5 6 7 8

9 10 11 12

13 14 15 16

17 18 19 20
"""