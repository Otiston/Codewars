def replace(arr):
    if type(arr) == list:
        for i in range(len(arr)):
            if type(arr[i]) != list:
                arr[i] = 1
            else:
                replace(arr[i])
    return arr

def same_structure_as(original,other):
    return replace(original)==replace(other)
