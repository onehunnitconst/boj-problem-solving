# 7785번: 회사에 있는 사람

from sys import stdin, stdout


def input_alt():
    return stdin.readline().rstrip()


def print_alt(s):
    return stdout.write(str(s) + "\n")

# 알고리즘 구현
def get_remain_employee_name(attendances):
    filtered = filter(lambda x: x[1] == 'enter', list(attendances.items()))
    names = map(lambda x: x[0], filtered)
    return sorted(names, reverse=True)

# 메인 함수
n = int(input_alt())
attendances = dict()

for _ in range(n):
    k, v = input_alt().split()
    attendances[k] = v

remain = get_remain_employee_name(attendances)

print('\n'.join(remain))
