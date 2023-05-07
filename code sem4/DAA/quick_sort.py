def swap(a,i,j):
    a[i],a[j]=a[j],a[i]
def partition(a, l, h):
    pivot = a[l]
    i = l
    j = h
    while i <= j:
        while i <= h and a[i] <= pivot:
            i += 1
        while j >= l and a[j] > pivot:
            j -= 1
        if i < j:
            swap(a, i, j)
    swap(a, l, j)
    return j



def qs(a,l,h):
    if(l<h):
        j=partition(a,l,h)
        print(a)
        qs(a,l,j)
        print(a)
        qs(a,j+1,h)
        print(a)
        

q=[7,4,1,9,5,3,0,2,6,8]
print(q)
qs(q,0,9)

print(q)