def getLogSettings(logs: list, m: int):
  min_log = 1
  max_log = 0
  result = 0

  for log in logs:
    max_log = max(max_log, log)

  while min_log <= max_log:
    ln = 0
    mid = int((min_log + max_log) / 2)

    for log in logs:
      if log > mid:
        ln = ln + log - mid
    
    if ln < m:
      max_log = mid - 1
    else:
      min_log = mid + 1
    
    result = max_log

  return result

n, m = list(map(int, input().split()))
logs = list(map(int, input().split()))

print(getLogSettings(logs, m))