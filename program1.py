def second_largest(arr):
    largest=float('-inf')
    second=float('-inf')
  for num in arr:
        if num > largest:
            second=largest
            largest=num
        elif num>second and num != largest:
            second=num
            return second   
arr=[10,5,8,20,15]
print=("second largest:",second largest:(arr))


