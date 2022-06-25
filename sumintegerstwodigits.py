def summ(arr):
  sum = 0
  for i in arr:
    if abs(i) >9 and abs(i)<100:
      sum = sum + i
  return sum
