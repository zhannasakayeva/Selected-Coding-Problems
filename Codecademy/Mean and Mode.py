def stats_finder(array):
  # Write your code here
  answer = []
  count = 0
  for i in array:
    count+=i
  answer.append(count/len(array))
  answer.append((max(set(array), key = array.count)))
  return answer
print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))
