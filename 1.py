z = input().split()
print(*list(map(lambda x: x.rjust(len(max(z, key=len)), "*"), z)), sep="\n")


def ugu():
    return None
