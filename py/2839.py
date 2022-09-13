def getSugarPack(n: int):
  sugar = n
  packs = 0

  while (sugar % 5 != 0) and (sugar >= 3):
    sugar = sugar - 3
    packs = packs + 1 

  if sugar % 5 == 0:
    packs = packs + (sugar / 5)
    return int(packs)
  else:
    return -1

n = int(input())

print(getSugarPack(n))