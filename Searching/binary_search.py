def binarySearchIterative(A, N):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (high + low)//2
        if A[mid] == N:
            return mid
        elif A[mid] > N:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binarySearchRecursive(A, N, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if A[mid] == N:
        return mid
    elif A[mid] > N:
        return binarySearchRecursive(A, N, low, mid - 1)
    else:
        return binarySearchRecursive(A, N, mid + 1, high)
