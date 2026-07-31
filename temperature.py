def celsius(x):
    return (x - 32) * 5 / 9


for x in range(-40, 101, 10):
    print(f"{x}°F = {celsius(x):.2f}°C")