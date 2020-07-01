import numpy as np

def maxOfArray(arr):
  return np.max(arr)


a = np.array([[2,4,5],[4,5,6]])
b = ["ñlk","kldks", 5]
c = "casa"
d = { "name" : 5}
l = (3,6)

arr = [a,b,c,d,l]

listVal = []
for i in range(0,4):
  listVal.append(arr[i])

print(len(listVal))
print(a)
print(a.shape)

