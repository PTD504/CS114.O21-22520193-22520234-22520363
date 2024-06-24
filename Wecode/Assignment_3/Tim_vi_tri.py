def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    need_search = list(map(int, input().split()))
    unordered_map = {}
    
    for i in range(m):
        unordered_map[need_search[i]] = -1
    
    for i in range(n):
        if arr[i] in unordered_map:
            unordered_map[arr[i]] = i
    
    for i in range(m):
        print(unordered_map[need_search[i]])

main()