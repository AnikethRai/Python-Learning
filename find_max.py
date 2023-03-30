def find_max(A):
    if len(A) == 0:
        return None
    largest = A[0]
    for i in range(len(A)-1):
        if largest < A[i+1]:
            largest = A[i+1]
    return largest

A = []
print(find_max(A))

        