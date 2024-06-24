def to_float(s):
    words = s.split()
    
    for word in words:
        try:
            return float(word[:-1])
        except ValueError:
            pass
    
    return 0

def main():
    st = input()
    lis = list(map(int, st.split()))
    
    n = len(lis)
    in_Store = 0.0
    online = 0.0
    
    for i in range(n):
        s = input()
        f = to_float(s) / 100
        
        if "lower" in s:
            in_Store += lis[i]
            online += float(lis[i] - lis[i] * f)
        else:
            in_Store += float(lis[i] - lis[i] * f)
            online += lis[i]
    
    money = float(input())
    
    if int(money - in_Store) >= 0 or int(money - online) >= 0:
        print("true")
    else:
        print("false")

main()