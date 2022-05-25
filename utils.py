def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)

def LcmOfArray(arr, idx):

    if (idx == len(arr) - 1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx + 1)
    return int(a * b / __gcd(a, b))
