# import math
# print(math.log2(0.0))
from main import 


test = [1, 2, 3, 4, 5]

arr1 = []
arr2 = []
print(sum(arr1))
start = 0
end = 4

while(start <= end):
  if sum(arr1) <= sum(arr2):
    arr1.append(test[start])
    start += 1
    print("START: ", start)
  else:
    arr2.append(test[end])
    end -= 1
    print("END: ", end)

print(arr1, arr2)
