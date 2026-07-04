guest = input()
host = input()
pile = input()
required_letters = sorted(guest + host)

if required_letters == sorted(pile):
    print("YES")
else:
    print("NO")
