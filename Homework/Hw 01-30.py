
def findSum(arr, N):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + findSum(arr[1:], N)

    # driver code


arr = []
arr = [1, 2, 3, 30, 5]

N = len(arr)

ans = findSum(arr, N)
print(ans)







