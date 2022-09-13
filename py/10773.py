class Account:
  def __init__(self):
    self.records = []
  def push(self, e):
    self.records.append(e)
  def pop(self):
    if len(self.records) > 0:
      self.records.pop()
  def sum(self):
    result = 0
    for index in range(len(self.records)):
      result = result + self.records[index]
    return result

k = int(input())
account = Account()

while k > 0:
  n = int(input())
  if n == 0:
    account.pop()
  else:
    account.push(n)
  k = k - 1

print(account.sum())