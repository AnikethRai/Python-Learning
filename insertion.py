def insertion_sort_asc(A):
    l = len(A)
    print(l)
    for j in range(1,l):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -=1
        A[i+1] = key
# def insertion_sort_desc(A):
#     for j in range(len(A) , 1):
#         key = A[j]
#         i = j-1
#         while i > 0 and  A[i] > key:
#             A[i] = A[i+1]
#             i = i-1
#         A[i+1] = key
#     return A

n = int(input('enter no.of elements:'))
A = [5,1,3,4,2]
# print('Enter elements in array A:')
# for k in range(n):
#     A.append(int(input()))
print(f'Unsorted array: {A}')
insertion_sort_asc(A)
print(*A)
# print(f'Descending order: {insertion_sort_desc(A)}')

