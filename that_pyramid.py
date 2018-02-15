x = 1
size = 8
for i in range(size):
    print((' ' * (size - 1)) + bin(x)[2:]
    .replace('0', ' ').replace('1', '*'))
    x ^= x << 1
