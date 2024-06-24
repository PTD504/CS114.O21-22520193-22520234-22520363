def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def checkAllDivisor(n, allSqrNumbers):
    if n in allSqrNumbers:
        return 0
        
    t = int(n ** 0.5)
    
    for i in range(2, t + 1):
        if n % i == 0:
            if i in allSqrNumbers or (n / i) in allSqrNumbers:
                return 0;
        
    return 1

def main():
    l, r = map(int, input().split())
    
    ans = 0
    
    # Find all square numbers more than or equal to l and less than or equal to r
    allSqrNumbers = {}
    i = 2
    
    while i * i <= r:
        allSqrNumbers[i * i] = 1
        i += 1
    
    # Find all special numbers in range [l, r]
    allSpecialNumbers = [checkAllDivisor(i, allSqrNumbers) for i in range(l, r + 1)]
    
    # Find all pairs(x, y) in range[l, r] that all x, y and x * y are special numbers
    for i in range(l, r):
        if allSpecialNumbers[i - l] == 0:
            continue
        for j in range(i + 1, r + 1):
            if allSpecialNumbers[j - l] == 0:
                continue
            if (gcd(j, i) == 1):
                ans += 1
    
    print(ans)
    
main()