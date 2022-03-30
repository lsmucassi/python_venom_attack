numbers = []
for i in range(10):
     num = float(input(f"Enter a float number [{i + 1}]: "))
     numbers.append(num)

print(sum(numbers))