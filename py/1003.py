t = int(input())

zeros = [1, 0]
ones = [0, 1]

for index in range(2, 41):
  zeros.append(zeros[index-2] + zeros[index-1])
  ones.append(ones[index-2] + ones[index-1])

while t > 0:
  n = int(input())
  print(str(zeros[n]) + ' ' + str(ones[n]))
  t = t - 1