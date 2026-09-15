def generate_subsets(nums):
    results=[]
    def backtrack(index,current):
        if index==len(nums):
            result.append(current.copy())
            return
        backtrack(index+1,current)
        current.append(nums[index])
        backtrack(index+1,current)
        current.pop()
    backtrack(0,[])
    return result 
nums=[1,2,3]
print(generate_subsets(nums))