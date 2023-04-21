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

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

def is_prime_number(num):
  if num <= 1:
    return False
  index = 2
  while index ** 2 <= num:
    if num % index == 0:
      return False
    index = index + 1
  return True

def goldbach_partition_count(num):
  result = 0
  index = 2
  while index <= n // 2:
    if is_prime_number(index) and is_prime_number(n - index):
      result = result + 1
    if index == 2:
      index = index + 1
    else:
      index = index + 2
  return result
    

t = int(input())

for _ in range(t):
  n = int(input())
  print(goldbach_partition_count(n))
