class Member:
  def __init__(self, id: int, age: int, name: str):
    self.id = id
    self.age = age
    self.name = name

  def getIdAndName(self):
    return str(self.age) + ' ' + self.name

n = int(input())

members = []

for index in range(n):
  age, name = input().split()
  member = Member(index, int(age), name)
  members.append(member)

members.sort(key=lambda member: member.age)

for index in range(n):
  print(members[index].getIdAndName())