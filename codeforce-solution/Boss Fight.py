import sys
from collections import Counter


def solve():
  input = sys.stdin.read
  data = input().split()
  if not data:
    return

  t = int(data[0])
  idx = 1
  out = []

  for _ in range(t):
    n = int(data[idx])
    a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
    idx += 1 + n

    total_sum = sum(a)
    counts = Counter(a)

    most_common_val, max_freq = counts.most_common(1)[0]
    max_safe_slots = (n - max_freq) + 1

    if max_freq <= max_safe_slots:
      out.append(str(total_sum))
    else:
      # The triggering duplicate card still deals damage, so we waste 1 less card
      wasted_cards = max_freq - max_safe_slots - 1
      max_damage = total_sum - (wasted_cards * most_common_val)
      out.append(str(max_damage))

  print("\n".join(out))


if __name__ == "__main__":
  solve()
