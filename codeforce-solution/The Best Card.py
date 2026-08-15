import sys


def is_prime(x):
  if x < 2:
    return False
  i = 2
  while i * i <= x:
    if x % i == 0:
      return False
    i += 1
  return True


def solve():
  input = sys.stdin.read
  data = input().split()
  if not data:
    return
  t = int(data[0])
  out = []
  for i in range(1, t + 1):
    n = int(data[i])
    if is_prime(n + 1):
      out.append("YES")
    else:
      out.append("NO")
  print("\n".join(out))


if __name__ == "__main__":
  solve()
