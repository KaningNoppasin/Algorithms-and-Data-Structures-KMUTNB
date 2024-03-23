def Binary_Search(data: list,target: int):
    if not data:
        return False
    mid = len(data) // 2
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return Binary_Search(data[:mid - 1],target)
    elif data[mid] < target:
        return Binary_Search(data[mid + 1:],target)

def Binary_Search_V2(data: list,target: int,low: int,high :int):
    if high - low < 0:
        return False
    mid = high - low
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return Binary_Search(data,target,low = low,high = mid - 1)
    elif data[mid] < target:
        return Binary_Search(data,target,low =  mid + 1,high = high)


lst = [i for i in range(0,10)]
print("data =>",lst)
# print(Binary_Search(lst,10))
print(Binary_Search_V2(lst,10))
