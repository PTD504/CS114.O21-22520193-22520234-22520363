def main():
    n = int(input())
    l = []
    
    n, count = int(n / 2), 0
    
    for i in range(n):
        c = int(input())
        l.append(c)
    
    if n & 1:
        c = input()
    
    for i in range(n - 1, -1, -1):
        c = int(input())
        if c != l[i]:
            count += 1
        if count > 1:
            print("FALSE")
            return
    print("TRUE")

main()