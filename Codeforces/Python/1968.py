import sys
input = sys.stdin.read

def main():
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        x = int(data[i])
        y = x - 1  # Choose y as x-1 for maximum (gcd(x, y) + y)
        results.append(str(y))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
