def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    m = len(A) if len(A) < len(B) else len(B)
    for i in range(m):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"