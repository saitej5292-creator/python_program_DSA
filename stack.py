def next_greater_element(arr):
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        stack=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            result[i]=stack[-1]
        stack.append(arr[i])
    return result
arr=[4,5,2,10]
print("array!",arr)
print("next greater element:",next_greater_element(arr))            
