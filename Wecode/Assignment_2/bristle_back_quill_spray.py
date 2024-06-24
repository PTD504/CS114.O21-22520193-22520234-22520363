def main():
    n = int(input())
    l = list(map(float, input().split()))
    
    x = int(input())
    y = int(input())
    
    z = float(input())
    
    Sum = 0
    listG = []
    
    for i in range(n):
        Sum += x
        if i == 0:
            listG.append(l[i])
        else:
            t = l[i] - l[i - 1]
            while listG:
                if listG[0] + z < l[i]:
                    listG.pop(0)
                else:
                    break
            Sum += y * len(listG)
            listG.append(l[i])
    
    print(Sum)

main()