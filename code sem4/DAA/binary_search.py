q = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def bs(a, l, h, k):
    if l > h:
        return -1  # Value not found
    else:
        mid = (l + h)//2
        if a[mid] == k:
            return mid
        elif k < a[mid]:
            return bs(a, l, mid-1, k)
        else:
            return bs(a, mid+1, h, k)

print(bs(q, 0, 8, 8))  # Output: 7
