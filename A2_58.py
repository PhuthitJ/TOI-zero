A, B, d, r = map(int, input().split())

def solve(A, B, d, r):
    if A > B:
        return False
    
    period = range(A, B + 1)
    cnt = 0

    for i in period:
        if i % d == r:
            cnt += 1
    
    return cnt

print(solve(A, B, d, r))