def prime_finder(n):
  prime_list = []
  for i in range(1, n+1):
    if i == 0 or i == 1:
      continue
    else:
      for j in range(2, int(i/2)+1):
        if i % j == 0:
          break
      else:
        prime_list.append(i)
  return prime_list
