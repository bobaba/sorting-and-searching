import helpers as test
import time

def bubbleSort(r, direction="asc"):
  s = len(r)
  for _ in range(s):
    for j in range(s-1):
      if direction == "asc":
        if r[j] > r[j+1]:
          r[j], r[j+1] = r[j+1], r[j]
      elif direction == "desc":
        if r[j] < r[j+1]:
          r[j], r[j+1] = r[j+1], r[j]

def selectionSort(r):
  s = len(r)
  for i in range(s):
    for j in range(i+1,s):
      if r[j] < r[i]:
        r[j],r[i] = r[i],r[j]


arr = test.randArr(10000)
start = time.time()
# print(arr)
# # bubbleSort(arr) # 10k = 18.6 seconds
selectionSort(arr) # 10k = 3.5 seconds
# print(arr)
end = time.time()
print(end - start)

