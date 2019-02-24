import time

def compare1(n):
  start = time.time
  min = n[0]
  for i in n:
    for j in n:
      if i < j and i < min:
        min = i
      elif i > j and j < min:
        min = j
      else:
        min = min
  end = time.time
  return min, end-start

def compare2(n):
  start = time.time
  min = n[0]
  for i in n:
    if i < min:
      min = i
  end = time.time
  return min, end-start


