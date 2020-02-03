from random import randrange

def randArr(size):
  r = []
  for _ in range(size):
    r.append(randrange(100))
  return r