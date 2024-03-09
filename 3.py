def nearby(data, places=1):
    result = list(filter(lambda x: '0' * places in x, data))
    return result

#
data = ["100100011", "100001681", "100001001", "100000101"]
print(nearby(data, places=4))

data = ["111", "101101110001011", "10"]
print(nearby(data, places=2))


def wert():
    return None
