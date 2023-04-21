# 17103: 골드바흐 파티션

# 골드바흐 파티션: 짝수 N을 두 소수의 합으로 나타내는 표현
# 테스트 케이스 T (1 <= T <= 100)
# 테스트 케이스마다 골드바흐 파티션의 수를 출력한다

# 입력 N (2 < N <= 10^6)

# 소수는 2를 제외하면 모두 홀수
# 만약 N = 18이라면 i = 3부터 i <= n/2 까지 반복문 돌림
# 4는 특수한 케이스
# 홀수만 검사하면 되므로 i = i + 2
# i, N-i가 모두 소수이면 골드바흐 파티션이 맞다

# 에라토스테네스의 체로 미리 1000001까지의 소수 테이블을 구해놓는다
# 그렇지 않고 일일이 판별하면 시간초과

from time import time
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

def get_prime_number_table(max):
  prime_number_table = [True for _ in range(max+1)]
  prime_numbers = []

  prime_number_table[0] = False
  prime_number_table[1] = False

  index = 2
  while index ** 2 <= max:
    if prime_number_table[index]:
      for sub in range(index+1, max+1):
        if sub % index == 0:
          prime_number_table[sub] = False
    prime_numbers.append(index)
    index = index + 1

  return prime_number_table, prime_numbers

def goldbach_partition_count(num, prime_number_table, prime_numbers):
  result = 0
  for index in prime_numbers:
    if index > num - index:
      break
    if prime_number_table[num - index]:
      result = result + 1
  return result

pnt, pns = get_prime_number_table(1000001)
t = int(input())

for _ in range(t):
  n = int(input())
  print(goldbach_partition_count(n, pnt, pns))