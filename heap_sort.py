__author__ = 'windows 7'

import heapify as hpfy

arr=[1,2,45,-1,0,90,99,4,89]
final_arr=[]
def heapSort(a):
    x=[]
    for i in range(len(a)/2,-1,-1):
        hpfy.heapify(a,i)
    final_arr.append(a[0])
    a[0],a[len(a)-1]=a[len(a)-1],a[0]
    a.pop()
    while(len(a)!=0):
        for i in range(len(a)/2,-1,-1):
            hpfy.heapify(a,i)
        final_arr.append(a[0])
        a[0],a[len(a)-1]=a[len(a)-1],a[0]
        a.pop()

heapSort(arr)

print final_arr[::-1]

#ask heap sort proper algorithm
