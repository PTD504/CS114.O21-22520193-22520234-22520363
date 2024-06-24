def main():
    l, m = map(int, input().split())
    vehicles = [tuple(input().split()) for _ in range(m)]
    ans, l, cur_side = 0, l * 100, "left"
    
    left = []
    right = []
    
    for strLength, side in vehicles:
        iLength = int(strLength)
        if side == "left":
            left.append(iLength)
        else:
            right.append(iLength)
            
    while left or right:
        cur_length = l
        
        if cur_side == "left":
            while left and cur_length >= left[0]:
                cur_length -= left.pop(0)
        else:
            while right and cur_length >= right[0]:
                cur_length -= right.pop(0)
        
        cur_side = "left" if cur_side == "right" else "right"
        ans += 1
    
    print(ans)

main()