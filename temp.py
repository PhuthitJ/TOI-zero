import sys

def count_trailing_zeros(num):
    count = 0
    i = 5
    while num // i >= 1:
        count += num // i
        i *= 5
    return count

def main():
    input = sys.stdin.read
    data = input().split()

    if not data: return
    n_cases = int(data[0])
    
    results = []
    
    for k in range(1, n_cases + 1):
        num = int(data[k])
        results.append(str(count_trailing_zeros(num)))
        
    print('\n'.join(results))

if __name__ == "__main__":
    main()