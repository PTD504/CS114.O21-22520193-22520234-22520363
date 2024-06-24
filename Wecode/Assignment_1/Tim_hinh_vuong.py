def main():
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    """
    M(x, y) -> M(x', y'), I(a, b)
    x' = a + (x - a)cos(anpha) - (y - b)sin(anpha) 
    y' = b + (x - a)sin(anpha) + (y + b)cos(anpha)
    """
    # Rotate B 90deg
    x1, y1 = xA - (yB - yA), yA + (xB - xA)

    x2, y2 = xB + (yA - yB), yB - (xA - xB)

    square1 = [(xA, yA), (x1, y1), (x2, y2), (xB, yB)]

    # Rotate B -90deg
    x2, y2 = xA + (yB - yA), yA - (xB - xA)
    
    x1, y1 = xB - (yA - yB), yB + (xA - xB)

    square2 = [(xA, yA), (xB, yB), (x1, y1), (x2, y2)]

    print(" ".join(map(str, square1)))
    print(" ".join(map(str, square2)))

main()